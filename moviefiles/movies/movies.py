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

@movie_blueprint.route('/genre_search', methods =['GET', 'POST'])
def genre_search():

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
            next_movie_url = None
            last_movie_url = None

            if movies_per_page < len(movies):

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
                handler_url = url_for('movie_bp.genre_search'),
                message = "Sorry, there are no listed movies in that genre."
            )
    else:
        return render_template(
            'movie/movies_by_genre.html',
            form = form,
            handler_url = url_for('movie_bp.genre_search')
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

@movie_blueprint.route('/actor_search', methods=['GET', 'POST'])
def actor_search():

    form = ActorSearchForm()

    title = "Movies by Actor"

    if form.validate_on_submit():

        actor = form.actor.data

        movies_per_page = 5

        try:
            movies = services.get_movie_by_actor(actor, repo.repo_instance)
            movies_to_show = movies[: movies_per_page]

            first_movie_url = None
            previous_movie_url = None
            next_movie_url = None
            last_movie_url = None

            if movies_per_page < len(movies):
                next_movie_url = url_for('movie_bp.actor', cursor=0 + movies_per_page, actor=actor)

                last_cursor = movies_per_page * int(len(movies) / movies_per_page)
                if len(movies) % movies_per_page == 0:
                    last_cursor -= movies_per_page
                last_movie_url = url_for('movie_bp.actor', cursor=last_cursor, actor=actor)

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
                'movie/movies_by_actor.html',
                form = form,
                handler_url = url_for('movie_bp.actor_search'),
                message = "Sorry, there are no listed movies for that actor."
            )
    else:
        return render_template(
            'movie/movies_by_actor.html',
            form = form,
            handler_url = url_for('movie_bp.actor_search')
        )

@movie_blueprint.route('/actor', methods=['GET'])
def actor():

    title = "Movies by Actor"

    movies_per_page = 5

    cursor = request.args.get('cursor')
    actor = request.args.get('actor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if actor is not None:

        total_movies = services.get_movie_by_actor(actor, repo.repo_instance)
        movies = total_movies[cursor:cursor + movies_per_page]

        first_movie_url = None
        previous_movie_url = None
        last_movie_url = None
        next_movie_url = None

        if cursor > 0:
            previous_movie_url = url_for('movie_bp.actor', cursor=cursor - movies_per_page, actor=actor)
            first_movie_url = url_for('movie_bp.actor', actor=actor)

        if cursor + movies_per_page < len(total_movies):
            next_movie_url = url_for('movie_bp.actor', cursor=cursor + movies_per_page, actor=actor)

            last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
            if len(total_movies) % movies_per_page == 0:
                last_cursor -= movies_per_page
            last_movie_url = url_for('movie_bp.actor', cursor=last_cursor, actor=actor)
        return render_template(
            'movie/movie.html',
            movies=movies,
            title=title,
            previous_movie_url=previous_movie_url,
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            next_movie_url=next_movie_url
        )

@movie_blueprint.route('/director_search', methods=['GET', 'POST'])
def director_search():

    form = DirectorSearchForm()

    title = "Movies by Director"

    if form.validate_on_submit():

        director = form.director.data

        movies_per_page = 5

        try:
            movies = services.get_movie_by_director(director, repo.repo_instance)
            movies_to_show = movies[: movies_per_page]

            first_movie_url = None
            previous_movie_url = None
            next_movie_url = None
            last_movie_url = None

            if movies_per_page < len(movies):
                next_movie_url = url_for('movie_bp.director', cursor=0 + movies_per_page, director=director)

                last_cursor = movies_per_page * int(len(movies) / movies_per_page)
                if len(movies) % movies_per_page == 0:
                    last_cursor -= movies_per_page
                last_movie_url = url_for('movie_bp.director', cursor=last_cursor, director=director)

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
                'movie/movies_by_director.html',
                form = form,
                handler_url = url_for('movie_bp.director_search'),
                message = "Sorry, there are no listed movies for that director."
            )
    else:
        return render_template(
            'movie/movies_by_director.html',
            form = form,
            handler_url = url_for('movie_bp.director_search')
        )

@movie_blueprint.route('/director', methods=['GET'])
def director():

    title = "Movies by Director"

    movies_per_page = 5

    cursor = request.args.get('cursor')
    director = request.args.get('director')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if director is not None:

        total_movies = services.get_movie_by_director(director, repo.repo_instance)
        movies = total_movies[cursor:cursor + movies_per_page]

        first_movie_url = None
        previous_movie_url = None
        last_movie_url = None
        next_movie_url = None

        if cursor > 0:
            previous_movie_url = url_for('movie_bp.director', cursor=cursor - movies_per_page, director=director)
            first_movie_url = url_for('movie_bp.director', director=director)

        if cursor + movies_per_page < len(total_movies):
            next_movie_url = url_for('movie_bp.director', cursor=cursor + movies_per_page, director=director)

            last_cursor = movies_per_page * int(len(total_movies) / movies_per_page)
            if len(total_movies) % movies_per_page == 0:
                last_cursor -= movies_per_page
            last_movie_url = url_for('movie_bp.director', cursor=last_cursor, director=director)
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