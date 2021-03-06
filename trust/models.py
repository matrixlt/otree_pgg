from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, Page, WaitPage
)
cu = c

doc = ''


class Constants(BaseConstants):
    players_per_group = 2
    num_rounds = 20
    name_in_url = 'my_trust'
    game_seq = 1


# randomly group at first round
class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.participant.role = p.id_in_group
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        public_points = p1.contribution*self.session.config["unit_more"] + \
            p2.contribution*self.session.config["unit_less"]

        if public_points >= self.session.config["threshold"]:
            profit = self.session.config["profit"]
        else:
            profit = 0
        p1.payoff = self.session.config["init_more"] - p1.contribution + profit
        p2.payoff = self.session.config["init_less"] - p2.contribution + profit
        if self.round_number == Constants.num_rounds:
            p1.participant.sum_points1 = p1.sum_payoff()
            p2.participant.sum_points1 = p2.sum_payoff()

    def is_successful(self):
        p1 = self.in_round(self.round_number - 1).get_player_by_id(1)
        p2 = self.in_round(self.round_number - 1).get_player_by_id(2)
        public_points = p1.contribution * self.session.config["unit_more"] + \
            p2.contribution*self.session.config["unit_less"]

        if public_points >= self.session.config["threshold"]:
            return "上一轮公共库中总分数为 {}，已达到目标值。".format(public_points)
        else:
            return "上一轮公共库中总分数为 {}，未达到目标值。".format(public_points)


class Player(BasePlayer):
    contribution = models.CurrencyField(widget=widgets.RadioSelect)

    def contribution_choices(self):
        init = self.session.config["init_more"] if self.id_in_group == 1 else self.session.config["init_less"]
        return currency_range(
            c(0),
            init,
            c(1)
        )

    def other_payoff(self):
        group = self.group
        if self.id_in_group == 1:
            return group.in_round(self.round_number - 1).get_player_by_id(2).payoff
        else:
            return group.in_round(self.round_number - 1).get_player_by_id(1).payoff

    def other_choice(self):
        group = self.group
        if self.id_in_group == 1:
            return group.in_round(self.round_number - 1).get_player_by_id(2).contribution
        else:
            return group.in_round(self.round_number - 1).get_player_by_id(1).contribution

    def sum_payoff(self):
        return sum(map(lambda x: x.payoff, self.in_all_rounds()))

    def my_choice(self):
        return self.in_round(self.round_number - 1).contribution

    def my_payoff(self):
        return self.in_round(self.round_number - 1).payoff

    def get_init(self):
        if self.id_in_group == 1:
            return self.session.config["init_more"]
        else:
            return self.session.config["init_less"]
