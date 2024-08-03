import asyncio
import aiohttp
import requests
import pandas as pd
import numpy as np
import joblib
import re
import nltk
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm

# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from app.tmdb import Tmdb
from database.IO_ops import IO_ops

class TrainModels:

    # Function to fetch movie keywords
    @classmethod
    async def fetch_keywords(cls, movie_id, api_key, session):
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords'
        retries = 10
        for _ in range(retries):
            try:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        keywords = [keyword['name'] for keyword in data.get('keywords', [])]
                        return ' '.join(keywords)
                    else:
                        await asyncio.sleep(1)  # Wait a bit before retrying
            except aiohttp.ClientOSError:
                await asyncio.sleep(1)  # Wait a bit before retrying
        return ''  # Return empty string if all retries fail

    # Function to fetch keywords for all movies concurrently
    @classmethod
    async def fetch_all_keywords(cls, movie_ids, api_key):
        async with aiohttp.ClientSession() as session:
            tasks = [cls.fetch_keywords(movie_id, api_key, session) for movie_id in movie_ids]
            return await asyncio.gather(*tasks)

    # Enhanced text preprocessing function
    @classmethod
    def preprocess_text(cls, text):
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\W', ' ', text)
        text = re.sub(r'\b\w{1,2}\b', '', text)
        tokens = text.split()
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in set(stopwords.words('english'))]
        return ' '.join(tokens)

    @classmethod
    async def train_models(cls):
        # Fetch TV shows and movies data
        df1 = await IO_ops.get_tv_shows(all=True)
        df2 = await IO_ops.get_movies(all=True)
        # Extract necessary columns and combine TV shows and movies
        movies_df = df2[['id', 'title', 'overview', 'release_date']]
        tv_shows = df1[['id', 'title', 'overview', 'release_date']]
        movies_df = pd.concat([movies_df, tv_shows], axis=0).dropna().reset_index(drop=True)

        # Preprocess the overview text
        tqdm.pandas()
        movies_df['overview'] = movies_df['overview'].progress_apply(cls.preprocess_text)

        # Fetch and preprocess keywords for each movie
        api_key = Tmdb.get_config()['auth_token']
        movie_ids = movies_df['id'].tolist()
        keywords_list = await cls.fetch_all_keywords(movie_ids, api_key)
        movies_df['keywords'] = [cls.preprocess_text(keywords) for keywords in keywords_list]

        # Combine overview and keywords into a single content field
        movies_df['content'] = movies_df['overview'] + ' ' + movies_df['keywords']

        # Convert the content text to TF-IDF features
        tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
        tfidf_matrix = tfidf.fit_transform(movies_df['content'])

        # Compute cosine similarity matrix
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Save the TF-IDF vectorizer, cosine similarity matrix, and movies DataFrame
        os.makedirs('saved_models', exist_ok=True)
        joblib.dump(tfidf, 'saved_models/tfidf_vectorizer.pkl', compress=3)
        joblib.dump(cosine_sim, 'saved_models/cosine_similarity_matrix.pkl', compress=3)
        movies_df.to_pickle('saved_models/movies_df.pkl', compression='bz2')

