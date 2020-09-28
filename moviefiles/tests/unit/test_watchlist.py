import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.watchlist import WatchList, Movie

@pytest.fixture
def watchlist():
    return WatchList()

def test_add():
    watchlist = WatchList()
    watchlist.add_movie("hello world")

    assert watchlist.size() == 0

    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))

    assert watchlist.size() == 1

def test_remove():
    watchlist = WatchList()
    watchlist.remove_movie(Movie("Moana", 2016))

    assert watchlist.size() == 0

    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.remove_movie(Movie("Moana", 2016))

    assert watchlist.size() == 0

def test_selection():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Avengers: Endgame", 2019))

    assert watchlist.select_movie_to_watch(1) == Movie("Avengers: Endgame", 2019)

    assert watchlist.select_movie_to_watch(2) == None

def test_first_select():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))

    assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)

def test_iteration():
    watchlist = WatchList()
    movies = [Movie("Moana", 2016), Movie("Avengers: Endgame", 2019), Movie("Ladybird", 2017)]
    for movie in movies:
        watchlist.add_movie(movie)
    iterator = iter(watchlist)

    assert next(iterator) == Movie("Moana", 2016)
    assert next(iterator) == Movie("Avengers: Endgame", 2019)
    assert next(iterator) == Movie("Ladybird", 2017)

    with pytest.raises(StopIteration):
        next(iterator)

def test_repeated_add():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Moana", 2016))
    assert watchlist.size() == 1







