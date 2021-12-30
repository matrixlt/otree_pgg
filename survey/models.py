
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    your_given_more = models.IntegerField(min=0)
    other_given_more = models.IntegerField(min=0)
    bottom_line_more = models.IntegerField(min=0)
    your_given_less = models.IntegerField(min=0)
    other_given_less = models.IntegerField(min=0)
    bottom_line_less = models.IntegerField(min=0)

    def your_given_more_max(self):
        return self.session.config["init_more"]

    def other_given_less_max(self):
        return self.session.config["init_more"]

    def bottom_line_less_max(self):
        return self.session.config["init_more"]

    def other_given_more_max(self):
        return self.session.config["init_less"]

    def bottom_line_more_max(self):
        return self.session.config["init_less"]

    def your_given_less_max(self):
        return self.session.config["init_less"]

    def end_points(self):
        participant = self.participant
        number_points1 = int(participant.sum_points1)
        number_points2 = int(participant.sum_points2)
        total_points = participant.sum_points1 + participant.sum_points2
        result = "你在游戏1中的分数为 {}，<br>在游戏2中的分数为 {}，<br>最终分数为 {}+{}={}，<br>最终报酬为 25+0.03*{}={}。".format(
            str(participant.sum_points1),str(participant.sum_points2),
            str(number_points1), str(number_points2), str(total_points),
            str(int(total_points)),str(participant.payoff_plus_participation_fee()))
        return result
