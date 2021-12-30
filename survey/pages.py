
from .models import *


class Survey(Page):
    form_model = 'player'
    form_fields = ['your_given_more', 'other_given_more', 'bottom_line_more',
                   'your_given_less', 'other_given_less', 'bottom_line_less']

    def vars_for_template(self):
        return dict(
            your_given_more="你的贡献（0-{}的整数）".format(
                self.player.session.config["init_more"]),
            other_given_more="对方的贡献（0-{}的整数）".format(
                self.player.session.config["init_less"]),
            bottom_line="你认为对方最少贡献多少，你才愿意贡献另一部分使得公共库总分数达到目标值{}？".format(
                self.player.session.config["threshold"]),
            your_given_less="你的贡献（0-{}的整数）".format(
                self.player.session.config["init_less"]),
            other_given_less="对方的贡献（0-{}的整数）".format(
                self.player.session.config["init_more"])
        )


class End(Page):
    form_model = 'player'


page_sequence = [Survey, End]
