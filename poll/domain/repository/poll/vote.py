from poll.domain.model.poll.group.votes import PollVotes
from poll.domain.model.poll.poll import Poll
from poll.domain.model.poll.vote import OptionPollVote
from poll.domain.model.user.user import User


class VotePollRepository:
    def vote_option(self, vote: OptionPollVote):
        raise NotImplementedError()

    def unvote_option(self, vote: OptionPollVote):
        raise NotImplementedError()

    def get_votes(self, poll: Poll, user: User) -> PollVotes:
        raise NotImplementedError()
