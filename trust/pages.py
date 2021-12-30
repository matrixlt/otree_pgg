
from .models import *


class Introduction(Page):
    form_model = 'player'

    def is_displayed(self):
        player = self.player
        return player.round_number == 1


class Send(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    body_text = '请耐心等待其他玩家选择'
    title_text = ""


class End(Page):
    form_model = 'player'

    def is_displayed(self):
        player = self.player
        return player.round_number == Constants.num_rounds


class Game1End(WaitPage):
    wait_for_all_groups = True
    body_text = '请耐心等待其他玩家结束游戏'
    title_text = ""

    def is_displayed(self):
        player = self.player
        return player.round_number == Constants.num_rounds


page_sequence = [Introduction, Send, ResultsWaitPage, End, Game1End]
