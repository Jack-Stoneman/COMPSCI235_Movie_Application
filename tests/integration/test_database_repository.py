import pytest

from COMPSCI235_Movie_Application.moviefiles.adapters.database_repository import SqlAlchemyRepository
from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Actor, Director
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import RepositoryException

def test_repository_can_retrieve_movies(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movies = repo.get_movies()

    print(movies)