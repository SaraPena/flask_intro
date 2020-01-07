from flask import Flask
from flask import render_template
import numpy as np
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice<int:ndice>')
def roll(ndice):
    # rolls = np.random.choice([1, 2, 3, 4, 5, 6],3)
    # return 'Your roll is '+ str(rolls)[1:-1]
    rolls = [randint(1,6) for _ in range(ndice)]
    return render_template(
        'roll_dice.html',
        rolls = rolls
    )

@app.route('/roll-dice')
def roll_empty(): 
    return """
    <h1>Add the amount of dice you would like to roll at the end of the url.<h1>
    <h2>Example: roll-dice8 <h2>
    <h3>TEST<h3>
    """

