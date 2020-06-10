from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Yuva Simha'

doc = """
This is game of big push
"""


class Constants(BaseConstants):
    name_in_url = 'bigpush_no_int'
    players_per_group = 7
    num_rounds = 10
    instructions_template = 'bigpush_no_int/instructions.html'
    round_instructions_template = 'bigpush_no_int/round_instructions.html'


class Subsession(BaseSubsession):

    random_max_rounds = models.IntegerField()

    def creating_session(self):
        if self.round_number==1:
            self.random_max_rounds = random.randint(7,10)
        else:
            self.random_max_rounds = self.in_round(self.round_number - 1).random_max_rounds






class Group(BaseGroup):


    sum_high_tech_investment = models.CurrencyField()

    individual_contribution = models.CurrencyField()








    def set_payoffs(self):

        high_tech_contribution = [p.high_tech_investment for p in self.get_players()]


        self.sum_high_tech_investment = sum(high_tech_contribution)

        for p in self.get_players():

            p.low_tech_investment = sum([+p.endowment, -p.high_tech_investment])
            if self.sum_high_tech_investment <300:
                p.payoff = p.high_tech_investment * 0.95 + (p.low_tech_investment)*1.03

            elif self.sum_high_tech_investment <400:
                p.payoff = p.high_tech_investment*1.03 + (p.low_tech_investment)*1.03

            elif self.sum_high_tech_investment <500:
                p.payoff = p.high_tech_investment*1.05 + (p.low_tech_investment)*1.03

            elif self.sum_high_tech_investment <600:
                p.payoff = p.high_tech_investment*1.07 + (p.low_tech_investment)*1.03

            else:
                p.payoff = p.high_tech_investment * 1.09 + (p.low_tech_investment) * 1.03





class Player(BasePlayer):

    name = models.StringField(label='Enter your name')
    age_player = models.IntegerField(label='Enter your age',min=10,max=100)
    endowment = models.CurrencyField()

    high_tech_investment = models.CurrencyField(label='Enter your investment for High tech sector', min=0,
                                             )

    def high_tech_investment_max(self):
        return self.endowment

    low_tech_investment = models.CurrencyField()