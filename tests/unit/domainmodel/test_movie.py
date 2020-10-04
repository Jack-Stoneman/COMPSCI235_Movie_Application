import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Director, Actor, Genre

@pytest.fixture
def movie():
    return Movie()

def test_movie():
    movie = Movie("Moana", 2016)
    print(movie)

    director = Director("Ron Clements")
    movie.director = director
    print(movie.director)

    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    print(movie.actors)

    movie.runtime_minutes = 107
    print("Movie runtime: {} minutes".format(movie.runtime_minutes))

def test_movie_methods():
    movie1 = Movie("A Star is Born", 2018)
    movie2 = Movie("A Star is Born", 1976)
    movie3 = Movie("Ghostbusters", 1984)

    assert movie1>movie2
    assert movie2<movie3
    assert movie1<movie3

def test_multiple_director():
    movie = Movie("Moana", 2016)
    director1 = Director("Ron Clements")
    director2 = Director("Martin Scorsese")

    movie.director = director1, director2

    print(movie.director)

    movie.director = director1

    print(movie.director)

def test_eq():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Moana", 2016)

    assert movie1 == movie2

def test_removal_methods():
    movie = Movie("Avengers: Endgame", 2019)

    actors = [Actor("Robert Downey Jr"), Actor("Chris Hemsworth"), Actor("Tom Holland")]
    genres = [Genre("Action"), Genre("Drama"), Genre("Superhero")]

    for actor in actors:
        movie.add_actor(actor)

    for genre in genres:
        movie.add_genre(genre)

    movie.remove_actor("Tom Holland")
    print(movie.actors)

    movie.remove_genre("Drama")
    print(movie.genres)


