import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                index += 1

    @property
    def dataset_of_movies(self) -> set:
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            movie_set = set()

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                movie_set.add(movie)
                genres = row['Genre'].split(",")
                for genre in genres:
                    movie.add_genre(Genre(genre))
                movie.description = row['Description']
                actors = row['Actors'].split(", ")
                for actor in actors:
                    movie.add_actor(Actor(actor))
                movie.runtime_minutes = int(row['Runtime (Minutes)'])

        return movie_set

    @property
    def dataset_of_actors(self) -> set:
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            actor_set = set()

            for row in movie_file_reader:
                actors = row['Actors'].split(",")
                for actor in actors:
                    actor_set.add(Actor(actor.strip()))


        return actor_set

    @property
    def dataset_of_directors(self) -> set:
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            director_set = set()

            for row in movie_file_reader:
                director = row['Director']
                director_set.add(Director(director))

        return director_set

    @property
    def dataset_of_genres(self) -> set:
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            genre_set = set()

            for row in movie_file_reader:
                genres = row['Genre'].split(",")
                for genre in genres:
                    genre_set.add(Genre(genre))


        return genre_set




