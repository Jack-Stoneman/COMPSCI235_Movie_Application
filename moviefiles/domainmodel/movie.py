from .genre import Genre
from .actor import Actor
from .director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title
        if type(release_year) is not int:
            self.__release_year = None
        if release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    @property
    def title(self) -> str:
        return self.__title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    def __repr__(self):
        return f"<Movie {self.__title}, {str(self.__release_year)}>"

    def __eq__(self, other):
        if type(other) is Movie:
            return self.__title == other.title and self.__release_year == other.release_year
        else:
            return False

    def __lt__(self, other):
        if type(other) is Movie:
            if self.__title == other.title:
                return self.__release_year < other.release_year
            else:
                return self.__title < other.title
        else:
            return False

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director):
        if type(director) is not Director:
            self.__director = None
        else:
            self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int:
            raise ValueError
        elif runtime_minutes < 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime_minutes

    def add_actor(self, actor):
        if actor == "" or type(actor) is not Actor:
            pass
        else:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        try:
            actor_index = self.__actors.index(actor)
            self.__actors.pop(actor_index)
        except ValueError:
            pass

    def add_genre(self, genre):
        if genre == "" or type(genre) is not Genre:
            pass
        else:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        try:
            genre_index = self.__genres.index(genre)
            self.__genres.pop(genre_index)
        except ValueError:
            pass











