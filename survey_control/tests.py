from otree.api import Currency as c, currency_range, expect, Bot, Submission
import survey_control.pages as pages


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Survey, dict(your_given_more=0, other_given_more=0, bottom_line_more=0)
        yield Submission(pages.End, check_html=False)
