import pandas as pd
import numpy as np
import os
from app.tmdb import Tmdb
import asyncio
from database.DatabaseUtil import *
from database.IO_ops import *
from database.models import Movies, TVShows, NowPlayingMovie, TopRatedMovie, PopularMovie, UpcomingMovie


class Scheduler:

    @classmethod
    async def tmdb_refresh(cls):
        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(None, Tmdb.get_movies, True),
            loop.run_in_executor(None, Tmdb.get_tv_shows, True),
            # loop.run_in_executor(None, Tmdb.get_rated_movies, True),
            loop.run_in_executor(None, Tmdb.get_now_playing_movies, True),
            loop.run_in_executor(None, Tmdb.get_top_rated_movies, True),
            loop.run_in_executor(None, Tmdb.get_popular_movies, True),
            loop.run_in_executor(None, Tmdb.get_upcoming_movies, True),
            # loop.run_in_executor(None, Tmdb.get_credits),
            # loop.run_in_executor(None, Tmdb.get_keywords)
        ]
        response, pending = await asyncio.wait(tasks)

        response_dict = {}
        [response_dict.update(t.result()) for t in response]

        movies = response_dict['movies']
        tv_shows = response_dict['tv_shows']
        # rated_movies = response_dict['rated_movies']
        now_playing_movies = response_dict['now_playing_movies']
        top_rated_movies = response_dict['top_rated_movies']
        popular_movies = response_dict['popular_movies']
        upcoming_movies = response_dict['upcoming_movies']
        cast = response_dict['cast']
        # crew = response_dict['crew']
        # keywords = response_dict['keywords']

        movies['release_date'] = movies['release_date'].astype('datetime64[ns]').dt.date
        tv_shows['first_air_date'] = tv_shows['first_air_date'].astype('datetime64[ns]').dt.date
        now_playing_movies['release_date'] = now_playing_movies['release_date'].astype('datetime64[ns]').dt.date
        top_rated_movies['release_date'] = top_rated_movies['release_date'].astype('datetime64[ns]').dt.date
        popular_movies['release_date'] = popular_movies['release_date'].astype('datetime64[ns]').dt.date
        upcoming_movies['release_date'] = upcoming_movies['release_date'].astype('datetime64[ns]').dt.date

        try:
            session = DatabaseUtil.get_postgres_session()
            IO_ops.save_to_postgres(movies, 'movies', session=session)
            IO_ops.save_to_postgres(tv_shows, 'tv_shows', session=session)
            IO_ops.save_to_postgres(now_playing_movies, 'now_playing_movies', session=session)
            IO_ops.save_to_postgres(top_rated_movies, 'top_rated_movies', session=session)
            IO_ops.save_to_postgres(popular_movies, 'popular_movies', session=session)
            IO_ops.save_to_postgres(upcoming_movies, 'upcoming_movies', session=session)
            session.commit()
        except Exception as err:
            session.rollback()
            raise err
        finally:
            DatabaseUtil.close_postgres_session(session)



