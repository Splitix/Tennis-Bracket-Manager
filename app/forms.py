from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf import FlaskForm
from random import randrange
import time

class FormNames(FlaskForm):
    names = TextAreaField('Names:')
    submit = SubmitField('Submit')

class Generator():
    def playerNames(self, names):
        players = names.splitlines()
        bracket = []
        for player in range(len(players)/2):
            random_index = randrange(len(players))
            player1 = players[random_index]
            players.remove(players[random_index])
            random_index = randrange(len(players))
            player2 = players[random_index]
            players.remove(players[random_index])
            bracket.append(player1 + ' vs ' + player2)

        return bracket
