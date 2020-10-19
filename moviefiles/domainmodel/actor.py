
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self._actor_full_name = None
        else:
            self._actor_full_name = actor_full_name
        self._colleague_list = []

    @property
    def actor(self) -> str:
        return self._actor_full_name

    @property
    def colleague_list(self) -> list:
        return self._colleague_list

    def __repr__(self):
        return f"<Actor {self._actor_full_name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self._actor_full_name == other.actor
        else:
            return False

    def __lt__(self, other):
        if type(other) is Actor:
            return self._actor_full_name < other.actor
        else:
            return False

    def __hash__(self):
        return hash(self._actor_full_name)

    def add_actor_colleague(self, colleague):
        self._colleague_list.append(colleague.actor)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.actor in self._colleague_list:
            return True
        else:
            return False







