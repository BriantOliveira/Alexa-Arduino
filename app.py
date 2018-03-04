import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

#Setting up Flask server
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent("YesIntent")

def next_round():

    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('round', numbers= numbers)
    session.attributes['numbers'] = numbers[::-1] #reverse
    return question(round_msg)

@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})

def answer(first, second, third):
    
