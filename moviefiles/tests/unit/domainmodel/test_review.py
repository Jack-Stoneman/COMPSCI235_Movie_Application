import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.review import Movie, Review

@pytest.fixture
def review():
    return Review

def test_review():
    movie = Movie("Moana", 2016)
    review_text = "This moviefiles was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)

    print(review.movie)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))