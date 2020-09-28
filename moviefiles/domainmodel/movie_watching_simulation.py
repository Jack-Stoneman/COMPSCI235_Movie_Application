from .watchlist import WatchList
from .review import Review
from .user import User

class MovieWatchingSimulation:

    def __init__(self, user: User, watchlist: WatchList):
        if type(watchlist) is WatchList:
            self.__watchlist = watchlist
        else:
            self.__watchlist = WatchList()
        if type(user) is User:
            self.__users = [user]
        else:
            raise Exception("user must be of type User")
        self.__reviews = []
        self.__watchedMovies = []

    @property
    def users(self) -> list:
        return self.__users

    @property
    def watchedMovies(self) -> list:
        return self.__watchedMovies

    @property
    def watchlist(self) -> WatchList:
        return self.__watchlist

    def add_user(self, user):
        if type(user) is User:
            self.__users.append(user)

    def watchMovie(self, index):
        movie = self.__watchlist.select_movie_to_watch(index)
        self.__watchlist.remove_movie(movie)
        if movie != None:
            self.__watchedMovies.append(movie)

    def add_review(self, review):
        if type(review) is Review:
            if review.movie in self.__watchedMovies:
                self.__reviews.append(review)
            else:
                return "Movie not yet watched."

    def get_review_by_movie(self, movie):
        review_list = []
        for review in self.__reviews:
            if review.movie == movie:
                review_list.append(review)
        return review_list

    def get_review_by_rating(self, rating):
        review_list = []
        if rating < 1 or rating > 10:
            raise Exception("Please enter a rating between 1 and 10")
        else:
            for review in self.__reviews:
                if review.rating == rating:
                    review_list.append(review)
        return review_list







