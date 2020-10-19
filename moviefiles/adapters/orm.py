from sqlalchemy import (
    Table, MetaData, Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Actor, Director, Genre

metadata = MetaData()

movies = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=False),
    Column('release_year', Integer, nullable=False),
    Column('description', String(255), nullable=False),
    Column('runtime_minutes', Integer, nullable=False),
    Column('director_id', ForeignKey('directors.id'))
)

genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
)

directors = Table(
    'directors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
)

movie_genre = Table(
    'movie_genre', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.id')),
    Column('genre_id', ForeignKey('genres.id'))
)

movie_actor = Table(
    'movie_actor', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', ForeignKey('movies.id')),
    Column('actor_id', ForeignKey('actors.id'))
)

def map_model_to_tables():
    actor_mapper = mapper(Actor, actors, properties={
        '_actor_full_name': actors.column.name
    })
    mapper(Director, directors, properties={
        '_director_full_name': directors.column.name
    })
    genre_mapper = mapper(Genre, genres, properties={
        '_genre': genres.column.name
    })
    mapper(Movie, movies, properties={
        '_title': movies.column.title,
        '_release_year': movies.column.release_year,
        '_description': movies.column.description,
        '_runtime_minutes': movies.column.runtime_minutes,
        '_director': relationship(Director, backref='_movie'),
        '_actors': relationship(
            actor_mapper,
            secondary=movie_actor,
            backref="_movie"
        ),
        '_genres': relationship(
            genre_mapper,
            secondary=movie_genre,
            backref="_movie"
        )
    })
