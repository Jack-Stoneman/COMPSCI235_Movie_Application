import pytest

from COMPSCI235_Movie_Application.moviefiles.movies import services as movie_services
from COMPSCI235_Movie_Application.moviefiles.movies.services import NonExistentMovieException

def test_can_get_movie(in_memory_repo):
    title = "Guardians of the Galaxy"
    year = 2014

    movie_as_dict = movie_services.get_movie(title, year, in_memory_repo)

    assert movie_as_dict['title'] == "Guardians of the Galaxy"
    assert movie_as_dict['release_year'] == 2014
    assert movie_as_dict['description'] == "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe."
    assert movie_as_dict['director'] == "James Gunn"
    assert movie_as_dict['actors'] == ["Chris Pratt", "Vin Diesel", "Bradley Cooper", "Zoe Saldana"]
    assert movie_as_dict['genres'] == ["Action", "Adventure", "Sci-Fi"]
    assert movie_as_dict['runtime_minutes'] == 121

def test_can_get_movie_by_title(in_memory_repo):
    title = "Split"

    movie_as_dict = movie_services.get_movie_by_title(title, in_memory_repo)

    print(movie_as_dict)

