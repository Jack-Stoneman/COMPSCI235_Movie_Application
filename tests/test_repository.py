import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Director, Actor
from COMPSCI235_Movie_Application.moviefiles.adapters.repository import RepositoryException

def test_movie_retrieval_by_title(in_memory_repo):
    movie = in_memory_repo.get_movie_by_title("Guardians of the Galaxy")
    assert movie == [Movie("Guardians of the Galaxy", 2014)]
