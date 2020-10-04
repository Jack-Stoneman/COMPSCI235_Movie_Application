""" Initialise Flask app """

import os

from flask import Flask

import COMPSCI235_Movie_Application.moviefiles.adapters.repository as repo
from COMPSCI235_Movie_Application.moviefiles.adapters.memory_repository import MemoryRepository

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')

    repo.repo_instance = MemoryRepository()

    return app
