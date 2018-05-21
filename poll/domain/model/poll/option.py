from poll.domain.model.base import Comparable


class PollOption:
    """
    Identify a single poll option among all options of all bot polls.
    Must not be presented to users.
    Ids are generated by repository.
    """
    def __init__(self, option_id: int):
        self.id = option_id


class PollOptionNumber(Comparable):
    """
    Identify a poll option within a poll.
    Must be used as option identifiers to users.
    Numbers are generated by repository.
    """
    def __init__(self, number: int):
        super().__init__(number, PollOptionNumber)
        self.number = number
