import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.genre import Genre

@pytest.fixture
def genre():
    return Genre()

def test_genre():
    genre1 = Genre("Horror")
    print(genre1)
    genre2 = Genre("")
    print(genre2)
