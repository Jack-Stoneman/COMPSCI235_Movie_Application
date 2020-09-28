from .movie import Movie

class WatchList:

    def __init__(self):
        self.__watchlist = []
        self.__iterator = 0

    def add_movie(self, movie):
        if type(movie) is Movie:
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie):
        try:
            movie_index = self.__watchlist.index(movie)
            self.__watchlist.pop(movie_index)
        except ValueError:
            pass

    def select_movie_to_watch(self, index):
        if index > len(self.__watchlist) - 1:
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if self.__watchlist != []:
            return self.__watchlist[0]
        else:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterator < len(self.__watchlist):
            result = self.__watchlist[self.__iterator]
            self.__iterator += 1
            return result
        else:
            raise StopIteration





