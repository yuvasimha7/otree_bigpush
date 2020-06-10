from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class index(Page):
    def is_displayed(self):
        return self.round_number == 1

class introduction(Page):
    def is_displayed(self):
        return self.round_number == 1
    'this is big push game'
    form_model = 'player'
    form_fields = ['name','age_player']

class myPage(Page):


    timeout_seconds = 120
    def is_displayed(self):

        if self.subsession.round_number<= self.subsession.random_max_rounds:

            if self.round_number==1:
                self.player.endowment = c(100)

            elif self.round_number >1:
                self.player.endowment = self.player.in_round(self.player.round_number - 1).payoff
            return self.player.endowment
        else:
            return False


    form_model = 'player'
    form_fields = ['high_tech_investment']





class justWaitPage(WaitPage):

    timeout_seconds = 75
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to contribute."
    template_name = 'bigpush_no_int/JustWaitPage.html'

class roundwaitpage(Page):
    pass


class results(Page):


    def is_displayed(self):
        return self.subsession.round_number <= self.subsession.random_max_rounds

class final(Page):
    def is_displayed(self):
        return self.round_number == self.subsession.random_max_rounds

    template_name = 'bigpush_no_int/final.html'
page_sequence = [index,introduction,myPage,justWaitPage,roundwaitpage,final]
