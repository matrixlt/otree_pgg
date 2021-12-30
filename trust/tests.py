from otree.api import Currency as c, currency_range, expect, Bot, Submission
import trust.pages as pages
from trust.models import Constants

class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number == 1:
            yield pages.Introduction
        yield pages.Send, dict(contribution=c(12))
        if self.player.round_number == Constants.num_rounds:
            yield Submission(pages.End, check_html=False)
