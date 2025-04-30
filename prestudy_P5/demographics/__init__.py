from otree.api import *
import csv
import os

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass

# ''' ONLY WHEN TESTING ON ITS OWN'''
# def creating_session(subsession):
#     for player in subsession.get_players():
#         participant = player.participant
#         participant.progress = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    ## Demographics
    age = models.IntegerField(
        verbose_name='What is your age?',
        min=0, max=100
    )
    gender = models.StringField(
        choices=['Female', 'Male', 'Other', 'Prefer not to say'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect
    )
    born = models.StringField(
        choices=['Yes', 'No'],
        widget=widgets.RadioSelect
    )
    # born = models.StringField()
    # income_ladder = models.IntegerField(
    #     choices=[i for i in range(1, 11)],
    #     blank=True,
    #     label="Where would you place yourself on this ladder?"
    # )
    education = models.StringField(
        choices=['No formal education/Early childhood education', 'Primary education (ages 5–12)',
                 'Lower secondary education (ages ~12–15)', 'Upper secondary education (ages ~15–18)',
                 'Post-secondary non-tertiary education (e.g., vocational training, certificates)',
                 'Short-cycle tertiary education (e.g., associate degree, advanced diploma)', 'Bachelor’s degree or equivalent',
                 'Master’s degree or equivalent', 'Doctoral degree (PhD) or equivalent'],
        verbose_name='What is the highest level of education you have completed?',
        widget=widgets.RadioSelect
    )
    rural = models.StringField(
        choices=["A rural area or village", 'Small or medium-sized town', 'Large town/city'],
        verbose_name='Would you say you live in...?',
        widget=widgets.RadioSelect
    )

    ## Comment field
    question_box = models.LongStringField(
        verbose_name='Could you tell us, in your own words, what the study was about?'
    )
    comment_box = models.LongStringField(
        verbose_name='If you have any additional comments on the study content or presentation please let us know in the box below.',
        blank = True  # Optional: allow it to be empty if no donation is made
    )


########### PAGES ############

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','born','education', 'rural']

    def vars_for_template(player: Player):

        return {
            'born_question': f"In which country were you born?",
        }

    # def before_next_page(player: Player, timeout_happened):


# class Ladder(Page):
#     form_model = 'player'
#     form_fields = ['income_ladder']
#
#     @staticmethod
#     def vars_for_template(player: Player):
#         return dict(
#             ladder_values=list(range(10, 0, -1)),  # From 10 to 1
#         )
#
#     def before_next_page(player: Player, timeout_happened):

class CommentBox(Page):
    form_model = 'player'
    form_fields = ['question_box', 'comment_box']

    def vars_for_template(player: Player):
        return {

        }



class Payment(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player: Player):
        return {
            'participation_fee': player.session.config['participation_fee'],
        }


class ProlificLink(Page):
    """
    This page redirects pp to prolific automatically with a javascript (don't forget to put paste the correct link!).
    There is a short text, the completion code and the link in case it is not automatic.
    """
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == C.NUM_ROUNDS:
            return True


page_sequence = [Demographics,
                 CommentBox,
                 Payment,
                 ProlificLink]
