import os
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import AbstractRepository, RepositoryException
from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Director, Actor
from COMPSCI235_Movie_Application.moviefiles.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._genres = list()
        self._actors = list()
        self._directors = list()
        self._users = list()

    def get_movies(self):
        return self._movies

    def get_movie(self, title: str, release_year: int):
        for movie in self._movies:
            if movie == Movie(title, int(release_year)):
                return movie
        return None

    def get_movie_by_title(self, title: str):
        result_list = []
        for movie in self._movies:
            if movie.title == title:
                result_list.append(movie)
        return result_list

    def get_movie_by_genre(self, genre: str):
        genre_list = genre.split(", ")
        result_list = []
        for i in range(len(genre_list)):
            genre_list[i] = Genre(str(genre_list[i]))
        for movie in self._movies:
            counter = 0
            for genre in genre_list:
                if genre in movie.genres:
                    counter += 1
                if counter == len(genre_list):
                    result_list.append(movie)
        return result_list

    def get_movie_by_actor(self, actor: str):
        actor_list = actor.split(", ")
        result_list = []
        for i in range(len(actor_list)):
            actor_list[i] = Actor(str(actor_list[i]))
        for movie in self._movies:
            counter = 0
            for actor in actor_list:
                if actor in movie.actors:
                    counter += 1
            if counter == len(actor_list):
                result_list.append(movie)
        return result_list

    def get_movie_by_director(self, director: str):
        result_list = []
        for movie in self._movies:
            if movie.director == Director(director):
                result_list.append(movie)
        return result_list

    def get_movie_by_year(self, release_year: int):
        result_list = []
        for movie in self._movies:
            if movie.release_year == int(release_year):
                result_list.append(movie)
        return result_list

    def get_genres(self):
        return self._genres

    def get_actors(self):
        return self._actors

    def get_directors(self):
        return self._directors

def populate(data_path, repo: MemoryRepository):
    reader = MovieFileCSVReader(data_path)
    reader.read_csv_file()
    repo._movies = reader.dataset_of_movies
    repo._genres = reader.dataset_of_genres
    repo._actors = reader.dataset_of_actors
    repo._directors = reader.dataset_of_directors


