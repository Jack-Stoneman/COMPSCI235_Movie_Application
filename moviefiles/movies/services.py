from typing import Iterable

from COMPSCI235_Movie_Application.moviefiles.adapters.repository import AbstractRepository
from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Actor, Genre, Director

class NonExistentMovieException(Exception):
    pass

def get_movie(title: str, release_year: str, repo: AbstractRepository):
    movie = repo.get_movie(title, release_year)

    if movie is None:
        raise NonExistentMovieException

    return movie_to_dict(movie)

def get_movie_by_title(title: str, repo: AbstractRepository):
    movies = repo.get_movie_by_title(title)

    if movies == []:
        raise NonExistentMovieException

    return movies_to_dict(movies)

def get_movie_by_genre(genres: list, repo: AbstractRepository):
    movies = repo.get_movie_by_genre(genres)

    if movies == []:
        raise NonExistentMovieException

    return movies_to_dict(movies)

def get_movie_by_actor(actors: list, repo: AbstractRepository):
    movies = repo.get_movie_by_actor(actors)

    if movies == []:
        raise NonExistentMovieException

    return movies_to_dict(movies)

def get_movie_by_director(director: Director, repo: AbstractRepository):
    movies = repo.get_movie_by_director(director)

    if movies == []:
        raise NonExistentMovieException

    return movies_to_dict(movies)

def get_movie_by_year(year: str, repo: AbstractRepository):
    movies = get_movie_by_year(year)

    if movies == []:
        raise NonExistentMovieException

    return movies_to_dict(movies)

def movie_to_dict(movie:Movie):
    movie_dict ={
        'title': movie.title,
        'release_year': movie.release_year,
        'description': movie.description,
        'director': movie.director,
        'actors': actors_to_dict(movie.actors),
        'genres': genres_to_dict(movie.genres),
        'runtime_minutes': movie.runtime_minutes
    }
    return movie_dict

def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]

def actor_to_dict(actor: Actor):
    actor_dict = {
        'full_name': actor.actor,
        'colleague_list': actor.colleague_list
    }
    return actor_dict

def actors_to_dict(actors: Iterable[Actor]):
    return [actor_to_dict(actor) for actor in actors]

#def genre_to_dict(genre: Genre):
 #   genre_dict = {
  #      'genre': genre.genre
   # }
    #return genre_dict

def genres_to_dict(genres: Iterable[Genre]):
    return [genre.genre for genre in genres]
