
class Genre:

    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre = None
        else:
            self.__genre = genre

    @property
    def genre(self) -> str:
        return self.__genre

    def __repr__(self):
        return f"<Genre {self.__genre}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.__genre == other.genre
        else:
            return False

    def __lt__(self, other):
        if type(other) is Genre:
            return self.__genre < other.genre
        else:
            return False

    def __hash__(self):
        return hash(self.__genre)
