""" Initialise Flask app """

import os

from flask import Flask

import COMPSCI235_Movie_Application.moviefiles.adapters.repository as repo
from COMPSCI235_Movie_Application.moviefiles.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('moviefiles', 'adapters', 'datafiles', 'Data1000Movies.csv')

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)


    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movies import movies
        app.register_blueprint(movies.movie_blueprint)



    return app
