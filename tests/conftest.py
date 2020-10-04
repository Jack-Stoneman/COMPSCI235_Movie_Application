import os
import pytest

from COMPSCI235_Movie_Application.moviefiles import create_app
from COMPSCI235_Movie_Application.moviefiles.adapters.memory_repository import MemoryRepository

@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    return repo

