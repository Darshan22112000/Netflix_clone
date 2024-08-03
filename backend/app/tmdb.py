import pandas as pd
import numpy as np
import requests
from pconf import Pconf
import os

from database.DatabaseUtil import DatabaseUtil
from database.models import Movies


class Tmdb:

    @classmethod
    def get_config(cls):
        # Read Current Directory relative to config files' path
        Pconf.env()
        current_file_path = os.path.realpath(__file__)
        current_directory = os.path.dirname(current_file_path)
        destination_directory = os.path.join(current_directory, '..', 'config')
        destination_file = os.path.join(destination_directory, "config.json")
        # print(destination_file)
        # Populate Pconf with json key-value pairs
        Pconf.file(destination_file, encoding='json')
        # Assign json key-value pairs to class variable
        config = Pconf.get()  # Pconf used to read config file
        return config

    @classmethod
    def get_movies(cls, scheduler=False):
        res = pd.DataFrame()
        for i in range(600):
            url = f"https://api.themoviedb.org/3/discover/movie?page={i+1}"
            auth_token = cls.get_config()['auth_token']
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {auth_token}"
            }
            response = requests.get(url, headers=headers)
            res = pd.concat([res, pd.DataFrame(response.json()['results'])], axis=0) if i>0 \
                                    else pd.DataFrame(response.json()['results'])
        # return {'movies': pd.DataFrame(response.json()['results'])} if scheduler else response
        res['release_date'] = res['release_date'].astype('datetime64[ns]').dt.date
        res = res.drop_duplicates(['id'])
        res = res.loc[res['release_date'].notnull()]
        res = res.loc[~res['release_date'].isnull()]
        res = res.dropna()
        res.reset_index(inplace=True)
        res = res.replace({'\r': ' ', '\n': ' '}, regex=True)
        return {'movies': res} if scheduler else response

    @classmethod
    def get_tv_shows(cls, scheduler=False):
        res = pd.DataFrame()
        for i in range(600):
            url = f"https://api.themoviedb.org/3/discover/tv?page={i + 1}"
            auth_token = cls.get_config()['auth_token']
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {auth_token}"
            }
            response = requests.get(url, headers=headers)
            res = pd.concat([res, pd.DataFrame(response.json()['results'])], axis=0) if i > 0 \
                else pd.DataFrame(response.json()['results'])
        res['first_air_date'] = res['first_air_date'].astype('datetime64[ns]').dt.date
        res = res.drop_duplicates(['id'])
        res = res.loc[res['first_air_date'].notnull()]
        res = res.loc[~res['first_air_date'].isnull()]
        res = res.dropna()
        res.reset_index(inplace=True)
        res = res.replace({'\r': ' ', '\n': ' '}, regex=True)
        return {'tv_shows': res} if scheduler else response

    @classmethod
    def get_rated_movies(cls, scheduler=False):
        url = "https://api.themoviedb.org/3/guest_session/guest_session_id/rated/movies"
        auth_token = cls.get_config()['auth_token']
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(url, headers=headers)
        return {'rated_movies': pd.DataFrame(response.json()['results'])} if scheduler else response

    @classmethod
    def get_now_playing_movies(cls, scheduler=False):
        url = "https://api.themoviedb.org/3/movie/now_playing"
        auth_token = cls.get_config()['auth_token']
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(url, headers=headers)
        return {'now_playing_movies': pd.DataFrame(response.json()['results'])} if scheduler else response

    @classmethod
    def get_popular_movies(cls, scheduler=False):
        url = "https://api.themoviedb.org/3/movie/popular"
        auth_token = cls.get_config()['auth_token']
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(url, headers=headers)
        return {'popular_movies': pd.DataFrame(response.json()['results'])} if scheduler else response

    @classmethod
    def get_top_rated_movies(cls, scheduler=False):
        url = "https://api.themoviedb.org/3/movie/top_rated"
        auth_token = cls.get_config()['auth_token']
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(url, headers=headers)
        return {'top_rated_movies': pd.DataFrame(response.json()['results'])} if scheduler else response


    @classmethod
    def get_upcoming_movies(cls, scheduler=False):
        url = "https://api.themoviedb.org/3/movie/upcoming"
        auth_token = cls.get_config()['auth_token']
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(url, headers=headers)
        return {'upcoming_movies': pd.DataFrame(response.json()['results'])} if scheduler else response

    @classmethod
    def get_credits(cls):
        session = DatabaseUtil.get_postgres_session()
        sq = session.query(Movies)
        df = pd.read_sql(sq.statement, session.bind)
        DatabaseUtil.close_postgres_session(session)
        auth_token = cls.get_config()['auth_token']
        cast1 = pd.DataFrame()
        crew1 = pd.DataFrame()
        for id in df['id']:
            url = f'https://api.themoviedb.org/3/movie/{id}/credits'
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {auth_token}"
            }
            response = requests.get(url, headers=headers)
            cast = pd.DataFrame(response.json()['cast'])
            crew = pd.DataFrame(response.json()['crew'])
            cast['id'] = response.json()['id']
            crew['id'] = response.json()['id']
            cast1 = pd.concat([cast1, cast], axis=0)
            crew1 = pd.concat([crew1, crew], axis=0)
        cast1.reset_index(inplace=True)
        crew1.reset_index(inplace=True)
        return {'cast': cast1, 'crew': crew1}

    @classmethod
    def get_keywords(cls):
        session = DatabaseUtil.get_postgres_session()
        sq = session.query(Movies)
        df = pd.read_sql(sq.statement, session.bind)
        DatabaseUtil.close_postgres_session(session)
        auth_token = cls.get_config()['auth_token']
        res = pd.DataFrame()
        for id in df['id']:
            url = f'https://api.themoviedb.org/3/movie/{id}/keywords'
            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {auth_token}"
            }
            response = requests.get(url, headers=headers)
            keywords = pd.DataFrame(response.json()['keywords'])
            keywords['id'] = response.json()['id']
            res = pd.concat([res, keywords], axis=0)
        res.reset_index(inplace=True)
        return {'keywords': res}

# Tmdb.get_top_rated_movies(scheduler=True)
# Tmdb.get_credits()


