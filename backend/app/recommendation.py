import asyncio
from http.client import HTTPException

import joblib
import requests
import pandas as pd
import numpy as np
import os
import difflib

class Recommendation:

    # Load pre-trained models and data
    @classmethod
    async def load_models(cls):
        # cwd = os.getcwd()
        # tfidf_path = os.path.join(cwd, 'saved_models', 'tfidf_vectorizer.pkl').replace("\\", '/')
        # cosine_path = os.path.join(cwd, 'saved_models', 'cosine_similarity_matrix.pkl').replace("\\", '/')
        # movie_path = os.path.join(cwd, 'saved_models', 'movies_df.pkl').replace("\\", '/')
        tfidf = joblib.load('app/saved_models/tfidf_vectorizer.pkl')
        cosine_sim = joblib.load('app/saved_models/cosine_similarity_matrix.pkl')
        movies_df = joblib.load('app/saved_models/movies_df.pkl')
        return tfidf, cosine_sim, movies_df

    @classmethod
    async def get_recommendations(cls, title):
        tfidf, cosine_sim, movies_df = await cls.load_models()
        title = title.lower()
        movies_df['title'] = movies_df['title'].str.lower()
        if title not in movies_df['title'].values:
            similar_movies = difflib.get_close_matches(title, movies_df['title'].unique().tolist())
            if similar_movies:
                title = similar_movies[0]
            else:
                return []
        idx = movies_df[movies_df['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        recommendations = movies_df['title'].iloc[movie_indices].tolist()
        return recommendations

# Test the recommendation function
# try:
#     print(asyncio.run(Recommendation.get_recommendations('The Matrix')))
# except:
#     print('Result Not Found')