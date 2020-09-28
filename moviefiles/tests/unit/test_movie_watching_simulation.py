import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie_watching_simulation import MovieWatchingSimulation, User, Review, WatchList

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie

@pytest.fixture
def movie_watching_simulation():
    return MovieWatchingSimulation()

def test_init():
    watchlist = WatchList()
    user = "James"
    with pytest.raises(Exception):
        watchingSimulation = MovieWatchingSimulation(user, watchlist)

def test_add_user():
    user = User("fred", "p@sS")
    watchSim = MovieWatchingSimulation(user, WatchList())
    watchSim.add_user(User("chadwick", "blckPnThEr"))
    assert watchSim.users == [user, User("chadwick", "blckPnThEr")]

def test_watch_and_review():
    user = User("fred", "p@sS")
    watchlist = WatchList()
    watchSim = MovieWatchingSimulation(user, watchlist)
    watchSim.watchlist.add_movie(Movie("Moana", 2016))
    watchSim.watchMovie(0)
    watchSim.add_review(Review(Movie("Moana", 2016), "Very fun moviefiles to watch with kids!", 8))

    assert watchSim.watchedMovies == [Movie("Moana", 2016)]
    assert watchSim.get_review_by_movie(Movie("Moana", 2016)) == [Review(Movie("Moana", 2016), "Very fun moviefiles to watch with kids!", 8)]
    assert watchSim.watchlist.size() == 0
    assert watchSim.get_review_by_rating(8) == [Review(Movie("Moana", 2016), "Very fun moviefiles to watch with kids!", 8)]

def test_illegal_rating():
    user = User("fred", "p@sS")
    watchlist = WatchList()
    watchSim = MovieWatchingSimulation(user, watchlist)
    with pytest.raises(Exception):
        watchSim.get_review_by_rating(11)