import csv
import os

from datetime import date
from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.security import generate_password_hash

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Actor, Genre, Director
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import AbstractRepository
from COMPSCI235_Movie_Application.moviefiles.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()

class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def get_movies(self) -> List[Movie]:
        movies = self._session_cm.session.query(Movie).all()

        return movies

    def get_movie(self, title: str, release_year: str) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter(Movie._title == title and Movie._release_year == release_year).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_movie_by_title(self, title: str) -> List[Movie]:
        try:
            movies = self._session_cm.session.query(Movie).filter(Movie._title == title).all()
        except NoResultFound:
            movies = []

        return movies

    def get_movie_by_genre(self, genre: str) -> List[Movie]:
        genre_list = genre.split(", ")
        genre_ids = list()
        for genre in genre_list:
            row = self._session_cm.session.execute('SELECT id FROM genres WHERE name = :genre', {'genre': genre}).fetchone()

            if row is not None:
                genre_ids.append(row[0])
        if genre_ids == []:
            return []
        else:
            movie_dict = {}
            movie_ids = []
            for id in genre_ids:
                rows = self._session_cm.session.execute('SELECT movie_id FROM movie_genre WHERE genre_id = :id', {'id': id}).all()
                for row in rows:
                    if row[0] in movie_dict:
                        movie_dict[row[0]].append(id)
                    else:
                        movie_dict[row[0]] = [id]
            for movie in movie_dict:
                if len(movie_dict[movie]) == len(genre_ids):
                    movie_ids.append(movie)
            movies = self._session_cm.session.query(Movie).filter(Movie._id.in_(movie_ids)).all()
            return movies

    def get_movie_by_actor(self, actor: str) -> List[Movie]:
        actor_list = actor.split(", ")
        actor_ids = list()
        for actor in actor_list:
            row = self._session_cm.session.execute('SELECT id FROM actors WHERE name = :actor', {'actor': actor}).fetchone()

            if row is not None:
                actor_ids.append(row[0])
        if actor_ids == []:
            return []
        else:
            movie_dict = {}
            movie_ids = []
            for id in actor_ids:
                rows = self._session_cm.session.execute('SELECT movie_id FROM movie_actor WHERE actor_id = :id',
                                                {'id': id}).all()
                for row in rows:
                    if row[0] in movie_dict:
                        movie_dict[row[0]].append(id)
                    else:
                        movie_dict[row[0]] = [id]
            for movie in movie_dict:
                if len(movie_dict[movie]) == len(actor_ids):
                    movie_ids.append(movie)
            movies = self._session_cm.session.query(Movie).filter(Movie._id.in_(movie_ids)).all()
            return movies

    def get_movie_by_director(self, director: str) -> List[Movie]:
        row = self._session_cm.session.execute('SELECT id FROM directors WHERE name = :director', {'director': director})
        if row is None:
            return []
        else:
            id = row[0]
            movies = self._session_cm.session.query(Movie).filter(Movie._director_id == id).all()
            return movies

    def get_movie_by_year(self, release_year: int) -> List[Movie]:
        movies = self._session_cm.session.query(Movie).filter(Movie._release_year == int(release_year)).all()
        return movies

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_genres(self) -> List[Genre]:
        genres = self._session_cm.session.query(Genre).all()
        return genres

    def get_actors(self) -> List[Actor]:
        actors = self._session_cm.session.query(Actor).all()
        return actors

    def get_directors(self) -> List[Director]:
        directors = self._session_cm.session.query(Director).all()
        return directors

def movie_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:

            movie_data=[row[0], row[1], row[6], row[3], row[7], row[4]]

            movie_data = [item.strip() for item in movie_data]

            yield movie_data

def genre_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        genre_set = set()

        # Read remaining rows from the CSV file.
        for row in reader:

            genres = row[2].split(",")

            for genre in genres:
                genre_set.add(genre)

        for genre in genre_set:

            genre_data = [genre]

            genre_data = [item.strip() for item in genre_data]

            yield genre_data


def actor_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        actor_set = set()

        # Read remaining rows from the CSV file.
        for row in reader:

            actors = row[2].split(",")

            for actor in actors:
                actor_set.add(actor)

        for actor in actor_set:
            actor_data = [actor]

            actor_data = [item.strip() for item in actor_data]

            yield actor_data

def director_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        director_set = set()

        # Read remaining rows from the CSV file.
        for row in reader:

            directors = row[2].split(",")

            for director in directors:
                director_set.add(director)

        for director in director_set:
            director_data = [director]

            director_data = [item.strip() for item in director_data]

            yield director_data

def movie_actor_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the CSV file.
        headers = next(reader)

        director_set = set()

        # Read remaining rows from the CSV file.
        for row in reader:

            directors = row[2].split(",")

            for director in directors:
                director_set.add(director)

        for director in director_set:
            director_data = [director]

            director_data = [item.strip() for item in director_data]

            yield director_data

def populate(engine: Engine, data_path: str):
    conn = engine.raw_connection()
    cursor = conn.cursor()

    insert_movies = """
        INSERT INTO movies (
        id, title, release_year, description, runtime_minutes, director)
        VALUES (?, ?, ?, ?, ?, ?)"""
    cursor.executemany(insert_movies, movie_record_generator(data_path))

    insert_genres = """
        INSERT INTO genres (
        name)
        VALUES (?)"""
    cursor.executemany(insert_genres, genre_record_generator(data_path))

    insert_actors = """
        INSERT INTO actors (
        name)
        VALUES (?)"""
    cursor.executemany(insert_actors, actor_record_generator(data_path))

    insert_directors = """
        INSERT INTO directors (
        name)
        VALUES (?)"""
    cursor.executemany(insert_directors, director_record_generator(data_path))

    conn.commit()
    conn.close()

