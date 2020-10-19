
class Genre:

    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self._genre = None
        else:
            self._genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    def __repr__(self):
        return f"<Genre {self._genre}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self._genre == other.genre
        else:
            return False

    def __lt__(self, other):
        if type(other) is Genre:
            return self._genre < other.genre
        else:
            return False

    def __hash__(self):
        return hash(self._genre)
