import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.user import User, Movie, Review

@pytest.fixture
def user():
    return User()

def test_user():
    user1 = User('Martin', 'pw12345')
    user2 = User('Ian', 'pw67890')
    user3 = User('Daniel', 'pw87465')
    print(user1)
    print(user2)
    print(user3)
