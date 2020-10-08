""" Initialise Flask app """

import os

from flask import Flask

import COMPSCI235_Movie_Application.moviefiles.adapters.repository as repo
from COMPSCI235_Movie_Application.moviefiles.adapters.memory_repository import MemoryRepository

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('C:', os.sep, 'Users', 'Jack', 'PycharmProjects', 'COMPSCI235-Assignment',
                              'COMPSCI235_Movie_Application', 'tests', 'datafiles')

    repo.repo_instance = MemoryRepository(data_path)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)


    return app
