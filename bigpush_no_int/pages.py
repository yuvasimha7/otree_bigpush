from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class preintro(Page):
    def is_displayed(self):
        return self.round_number == 1

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    'this is big push game'
    form_model = 'player'
    form_fields = ['name','age_player']

class MyPage(Page):


    timeout_seconds = 120
    def is_displayed(self):

        if self.subsession.round_number<= self.subsession.random_max_rounds:

            if self.round_number==1:
                self.player.endowment = c(350)

            elif self.round_number >1:
                self.player.endowment = self.player.in_round(self.player.round_number - 1).payoff
            return self.player.endowment
        else:
            return False


    form_model = 'player'
    form_fields = ['high_tech_investment']





class JustWaitPage(WaitPage):

    timeout_seconds = 75
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to contribute."
    template_name = 'bigpush_no_int/JustWaitPage.html'

class roundwaitpage(Page):
    pass


class Results(Page):


    def is_displayed(self):
        return self.subsession.round_number <= self.subsession.random_max_rounds

class final(Page):
    def is_displayed(self):
        return self.round_number == self.subsession.random_max_rounds

    template_name = 'bigpush_no_int/final.html'
page_sequence = [preintro,Introduction,MyPage,JustWaitPage,roundwaitpage,final]
