import os
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import AbstractRepository, RepositoryException
from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Director, Actor
from COMPSCI235_Movie_Application.moviefiles.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

class MemoryRepository(AbstractRepository):

    def __init__(self):
        reader = MovieFileCSVReader('datafiles/Data1000Movies.csv')
        self.__movies = list(reader.dataset_of_movies)
        self.__genres = list(reader.dataset_of_genres)
        self.__actors = list(reader.dataset_of_actors)
        self.__directors = list(reader.dataset_of_directors)

    def get_movies(self):
        return self.__movies

    def get_movie_by_title(self, title: str):
        result_list = []
        for movie in self.__movies:
            if movie.title == title:
                result_list.append(movie)
        return result_list

    def get_movie_by_genre(self, genre: Genre):
        result_list = []
        for movie in self.__movies:
            if genre in movie.genres:
                result_list.append(movie)
        return result_list

    def get_movie_by_actor(self, actor: Actor):
        result_list = []
        for movie in self.__movies:
            if actor in movie.actors:
                result_list.append(movie)
        return result_list

    def get_movie_by_director(self, director: Director):
        result_list = []
        for movie in self.__movies:
            if movie.director == director:
                result_list.append(movie)
        return result_list

    def get_movie_by_year(self, release_year: int):
        result_list = []
        for movie in self.__movies:
            if movie.release_year == int(release_year):
                result_list.append(movie)
        return result_list

    def get_genres(self):
        return self.__genres

    def get_actors(self):
        return self.__actors

    def get_directors(self):
        return self.__directors





