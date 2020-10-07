
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name
        self.__colleague_list = []

    @property
    def actor(self) -> str:
        return self.__actor_full_name

    @property
    def colleague_list(self) -> list:
        return self.__colleague_list

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name == other.actor
        else:
            return False

    def __lt__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name < other.actor
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleague_list.append(colleague.actor)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.actor in self.__colleague_list:
            return True
        else:
            return False







