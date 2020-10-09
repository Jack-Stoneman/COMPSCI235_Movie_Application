from flask import Blueprint, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

import COMPSCI235_Movie_Application.moviefiles.movies.services as services
import COMPSCI235_Movie_Application.moviefiles.adapters.repository as repo

movie_blueprint = Blueprint('movie_bp', __name__)

@movie_blueprint.route('/show_all', methods=['GET'])
def show_all():
    movies_per_page = 5

    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    total_movies = services.get_movies(repo.repo_instance)

    movies = total_movies[cursor:cursor + movies_per_page]

    first_movie_url = None
    previous_movie_url = None
    last_movie_url = None
    next_movie_url = None

    if cursor > 0:
        previous_movie_url = url_for('movie_bp.show_all', cursor = cursor - movies_per_page)
        first_movie_url = url_for('movie_bp.show_all')

    if cursor + movies_per_page < len(total_movies):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('movie_bp.show_all', cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
        if len(total_movies) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('movie_bp.show_all', cursor=last_cursor)

    return render_template(
        'movie/movie.html',
        movies = movies,
        previous_movie_url = previous_movie_url,
        first_movie_url = first_movie_url,
        next_movie_url = next_movie_url,
        last_movie_url = last_movie_url
    )

@movie_blueprint.route('/movie_search', methods=['GET', 'POST'])
def movie_search():
    form = MovieSearchForm()

    if form.validate_on_submit():
        title = form.movie_title.data
        movies = services.get_movie_by_title(title, repo.repo_instance)
        return render_template(
            'movie/movie.html',
            movies = movies
        )
    else:
        return render_template(
            'movie/movie_search.html',
            form = form,
            handler_url = url_for('movie_bp.movie_search')
        )

@movie_blueprint.route('/movies_by_genre', methods =['GET', 'POST'])
def movies_by_genre():
    form = GenreSearchForm()

    if form.validate_on_submit():
        genre = form.genre.data
        movies = services.get_movie_by_genre(genre, repo.repo_instance)
        return render_template(
            'movie/movie.html',
            movies = movies
        )
    else:
        return render_template(
            'movie/movies_by_genre.html',
            form = form,
            handler_url = url_for('movie_bp.movies_by_genre')
        )

class MovieSearchForm(FlaskForm):

    movie_title = StringField('Title')

    submit = SubmitField('Search')

class GenreSearchForm(FlaskForm):

    genre = StringField('Genre(s)')

    submit = SubmitField('Search')