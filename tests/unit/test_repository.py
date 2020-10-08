import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Director, Actor
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import RepositoryException

def test_movie_retrieval_by_title(in_memory_repo):
    movie = in_memory_repo.get_movie_by_title("Guardians of the Galaxy")
    assert movie == [Movie("Guardians of the Galaxy", 2014)]

def test_movie_retrieval_by_single_genre(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_genre('Animation')
    print(movie_list)

def test_movie_retrieval_by_multiple_genres(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_genre('Drama, Thriller')
    print(movie_list)

def test_movie_retrieval_by_single_actor(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_actor('Tom Cruise')
    print(movie_list)

def test_movie_retrieval_by_multiple_actors(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_actor("Chris Pratt, Zoe Saldana")
    print(movie_list)

def test_movie_retrieval_by_director(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_director("Christopher Nolan")
    print(movie_list)

def test_movie_retrieval_by_year(in_memory_repo):
    movie_list = in_memory_repo.get_movie_by_year('2012')
    print(movie_list)

def test_genre_retrieval(in_memory_repo):
    genre_list = in_memory_repo.get_genres()
    print(genre_list)