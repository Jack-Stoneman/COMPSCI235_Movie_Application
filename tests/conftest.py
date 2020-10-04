import os
import pytest

from COMPSCI235_Movie_Application.moviefiles import create_app
from COMPSCI235_Movie_Application.moviefiles.adapters.memory_repository import MemoryRepository

TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'Jack', 'PycharmProjects', 'COMPSCI235-Assignment',
                              'COMPSCI235_Movie_Application', 'tests', 'datafiles')

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository(TEST_DATA_PATH)
    return repo

