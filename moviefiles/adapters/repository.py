import abc

from COMPSCI235_Movie_Application.moviefiles.domainmodel.movie import Movie, Genre, Actor, Director

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_movies(self):
        """ Displays all movies """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_title(self, title: str):
        """ Searches for movies based on title """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_genre(self, genre: Genre):
        """ Searches for movies based on genre """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_actor(self, actor: Actor):
        """ Searches for movies based on starring actor """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_director(self, director: Director):
        """ Searches for movies based on director """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_year(self, release_year: int):
        """ Searches for movies based on release year """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self):
        """ Displays all genres """
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self):
        """ Displays all actors """
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self):
        """ Displays all directors """
        raise NotImplementedError


