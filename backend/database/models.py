from sqlalchemy import Date, Column, String, Integer, TIMESTAMP, TIME, Boolean, Text, Float

from database.DatabaseUtil import DatabaseUtil
# Project Imports
from database.base_model import BaseModel

config = DatabaseUtil.get_config()
BaseModel.init_base(config)

class Movies(BaseModel.base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    original_language = Column(String, nullable=False)
    original_title = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    release_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    video = Column(Boolean, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)

class TVShows(BaseModel.base):
    __tablename__ = 'tv_shows'

    id = Column(Integer, primary_key=True, autoincrement=True)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    origin_country = Column(String, nullable=False)
    original_language = Column(String, nullable=False)
    original_name = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    first_air_date = Column(Date, nullable=False)
    name = Column(String, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)

class NowPlayingMovie(BaseModel.base):
    __tablename__ = 'now_playing_movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    original_language = Column(String, nullable=False)
    original_title = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    release_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    video = Column(Boolean, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)

class PopularMovie(BaseModel.base):
    __tablename__ = 'popular_movies'

    id = Column(Integer, primary_key=True, autoincrement=False)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    original_language = Column(String, nullable=False)
    original_title = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    release_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    video = Column(Boolean, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)


class TopRatedMovie(BaseModel.base):
    __tablename__ = 'top_rated_movies'

    id = Column(Integer, primary_key=True, autoincrement=False)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    original_language = Column(String, nullable=False)
    original_title = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    release_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    video = Column(Boolean, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)


class UpcomingMovie(BaseModel.base):
    __tablename__ = 'upcoming_movies'

    id = Column(Integer, primary_key=True, autoincrement=False)
    adult = Column(Boolean, nullable=False)
    backdrop_path = Column(String, nullable=True)
    genre_ids = Column(String, nullable=False)  # Storing as a comma-separated string
    original_language = Column(String, nullable=False)
    original_title = Column(String, nullable=False)
    overview = Column(Text, nullable=True)
    popularity = Column(Float, nullable=False)
    poster_path = Column(String, nullable=True)
    release_date = Column(Date, nullable=False)
    title = Column(String, nullable=False)
    video = Column(Boolean, nullable=False)
    vote_average = Column(Float, nullable=False)
    vote_count = Column(Integer, nullable=False)