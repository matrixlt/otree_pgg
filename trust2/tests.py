from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Introduction
        yield Send, dict(contribution=12)
        yield Results