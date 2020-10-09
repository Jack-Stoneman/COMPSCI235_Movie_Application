from flask import Blueprint, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

import COMPSCI235_Movie_Application.moviefiles.movies.services as services
import COMPSCI235_Movie_Application.moviefiles.adapters.repository as repo

movie_blueprint = Blueprint('movie_bp', __name__)

@movie_blueprint.route('/show_all', methods=['GET'])
def show_all():
    movies_per_page = 5

    title = "All Movies"

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
        next_movie_url = url_for('movie_bp.show_all', cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
        if len(total_movies) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('movie_bp.show_all', cursor=last_cursor)

    return render_template(
        'movie/movie.html',
        title = title,
        movies = movies,
        previous_movie_url = previous_movie_url,
        first_movie_url = first_movie_url,
        next_movie_url = next_movie_url,
        last_movie_url = last_movie_url
    )

@movie_blueprint.route('/movie_search', methods=['GET', 'POST'])
def movie_search():
    form = MovieSearchForm()

    main_title = "Movies by Title"

    if form.validate_on_submit():
        movies_per_page = 5

        cursor = request.args.get('cursor')

        if cursor is None:
            cursor = 0
        else:
            cursor = int(cursor)

        title = form.movie_title.data
        try:
            total_movies = services.get_movie_by_title(title, repo.repo_instance)
            movies = total_movies[cursor:cursor + movies_per_page]

            first_movie_url = None
            previous_movie_url = None
            last_movie_url = None
            next_movie_url = None

            if cursor > 0:
                previous_movie_url = url_for('movie_bp.movie_search', cursor=cursor - movies_per_page)
                first_movie_url = url_for('movie_bp.movie_search')

            if cursor + movies_per_page < len(total_movies):
                next_movie_url = url_for('movie_bp.movie_search', cursor=cursor + movies_per_page)

                last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
                if len(total_movies) % movies_per_page == 0:
                    last_cursor -= movies_per_page
                last_movie_url = url_for('movie_bp.movie_search', cursor=last_cursor)
            return render_template(
                'movie/movie.html',
                movies = movies,
                title = main_title,
                previous_movie_url = previous_movie_url,
                first_movie_url = first_movie_url,
                last_movie_url = last_movie_url,
                next_movie_url = next_movie_url
            )
        except services.NonExistentMovieException:
            return render_template(
                'movie/movie_search.html',
                form = form,
                handler_url = url_for('movie_bp.movie_search'),
                message = "Sorry, there are no listed movies with that title."
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

    title = "Movies by Genre"

    if form.validate_on_submit():

        genre = form.genre.data

        movies_per_page = 5

        try:
            movies = services.get_movie_by_genre(genre, repo.repo_instance)
            movies_to_show = movies[: movies_per_page]

            first_movie_url = None
            previous_movie_url = None
            next_movie_url = url_for('movie_bp.genre', cursor=0 + movies_per_page, genre=genre)

            last_cursor = movies_per_page * int(len(movies) / movies_per_page)
            if len(movies) % movies_per_page == 0:
                last_cursor -= movies_per_page
            last_movie_url = url_for('movie_bp.genre', cursor=last_cursor, genre=genre)

            return render_template(
                'movie/movie.html',
                movies=movies,
                title=title,
                previous_movie_url=previous_movie_url,
                first_movie_url=first_movie_url,
                last_movie_url=last_movie_url,
                next_movie_url=next_movie_url
            )
        except services.NonExistentMovieException:
            return render_template(
                'movie/movies_by_genre.html',
                form = form,
                handler_url = url_for('movie_bp.movies_by_genre'),
                message = "Sorry, there are no listed movies in that genre."
            )
    else:
        return render_template(
            'movie/movies_by_genre.html',
            form = form,
            handler_url = url_for('movie_bp.movies_by_genre')
        )

@movie_blueprint.route('/genre', methods=['GET'])
def genre():

    title = "Movies by Genre"

    movies_per_page = 5

    cursor = request.args.get('cursor')
    genre = request.args.get('genre')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if genre is not None:

        total_movies = services.get_movie_by_genre(genre, repo.repo_instance)
        movies = total_movies[cursor:cursor + movies_per_page]

        first_movie_url = None
        previous_movie_url = None
        last_movie_url = None
        next_movie_url = None

        if cursor > 0:
            previous_movie_url = url_for('movie_bp.genre', cursor=cursor - movies_per_page, genre=genre)
            first_movie_url = url_for('movie_bp.genre', genre=genre)

        if cursor + movies_per_page < len(total_movies):
            next_movie_url = url_for('movie_bp.genre', cursor=cursor + movies_per_page, genre=genre)

            last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
            if len(total_movies) % movies_per_page == 0:
                last_cursor -= movies_per_page
            last_movie_url = url_for('movie_bp.genre', cursor=last_cursor, genre=genre)
        return render_template(
            'movie/movie.html',
            movies=movies,
            title=title,
            previous_movie_url=previous_movie_url,
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            next_movie_url=next_movie_url
        )



class MovieSearchForm(FlaskForm):

    movie_title = StringField('Title')

    submit = SubmitField('Search')

class GenreSearchForm(FlaskForm):

    genre = StringField('Genre(s)')

    submit = SubmitField('Search')

class ActorSearchForm(FlaskForm):

    actor = StringField('Actor(s)')

    submit = SubmitField('Search')

class DirectorSearchForm(FlaskForm):

    director = StringField('Director')

    submit = SubmitField('Search')