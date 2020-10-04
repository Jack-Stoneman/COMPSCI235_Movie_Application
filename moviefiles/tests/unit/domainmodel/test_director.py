import pytest

from COMPSCI235_Movie_Application.moviefiles.domainmodel.director import Director

@pytest.fixture
def director():
    return Director()

def test_director():
    director1 = Director("Cameron Diaz")
    director2 = Director("Angelina Jolie")
    director3 = Director("Brad Pitt")
    print(director1 > director2)
    print(director1 > director3)
    print(director2 < director3)









