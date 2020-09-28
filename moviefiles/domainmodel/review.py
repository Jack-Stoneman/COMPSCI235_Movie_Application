from datetime import datetime

from .movie import Movie

class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int, timestamp = None):
        if type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text
        if type(rating) is not int:
            self.__rating = None
        if rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating
        if type(timestamp) is not datetime:
            self.__timestamp = None
        else:
            self.__timestamp = timestamp

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<{self.__movie}, Rating: {self.__rating}/10, Timestamp: {self.__timestamp}>"

    def __eq__(self, other):
        return self.__movie == other.movie and self.__review_text == other.review_text \
        and self.__rating == other.rating and self.__timestamp == other.timestamp





