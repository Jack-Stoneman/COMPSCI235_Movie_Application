from .genre import Genre
from .actor import Actor
from .director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self._title = None
        else:
            self._title = title
        if type(release_year) is not int:
            self._release_year = None
        if release_year < 1900:
            self._release_year = None
        else:
            self._release_year = release_year
        self._description = None
        self._director = None
        self._actors = []
        self._genres = []
        self._runtime_minutes = None

    @property
    def title(self) -> str:
        return self._title.strip()

    @property
    def release_year(self) -> int:
        return self._release_year

    def __repr__(self):
        return f"<Movie {self._title}, {str(self._release_year)}>"

    def __eq__(self, other):
        if type(other) is Movie:
            return self._title == other.title and self._release_year == other.release_year
        else:
            return False

    def __lt__(self, other):
        if type(other) is Movie:
            if self._title == other.title:
                return self._release_year < other.release_year
            else:
                return self._title < other.title
        else:
            return False

    def __hash__(self):
        return hash((self._title, self._release_year))

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description):
        if description == "" or type(description) is not str:
            self._description = None
        else:
            self._description = description.strip()

    @property
    def director(self) -> Director:
        return self._director

    @director.setter
    def director(self, director):
        if type(director) is not Director:
            self._director = None
        else:
            self._director = director

    @property
    def actors(self) -> list:
        return self._actors

    @property
    def genres(self) -> list:
        return self._genres

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int:
            raise ValueError
        elif runtime_minutes < 0:
            raise ValueError
        else:
            self._runtime_minutes = runtime_minutes

    def add_actor(self, actor):
        if actor == "" or type(actor) is not Actor:
            pass
        else:
            self._actors.append(actor)

    def remove_actor(self, actor):
        try:
            actor_index = self._actors.index(actor)
            self._actors.pop(actor_index)
        except ValueError:
            pass

    def add_genre(self, genre):
        if genre == "" or type(genre) is not Genre:
            pass
        else:
            self._genres.append(genre)

    def remove_genre(self, genre):
        try:
            genre_index = self._genres.index(genre)
            self._genres.pop(genre_index)
        except ValueError:
            pass











