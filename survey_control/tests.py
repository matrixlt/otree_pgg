from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Survey, dict(your_given_more=0, other_given_more=0, bottom_line_more=0)
