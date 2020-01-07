from flask import Flask
from flask import render_template
import numpy as np
from random import randint

from flask import request

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import 

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

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods = ['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting = greeting)   


@app.route('/predict-spam')
def prediction_input():
    return render_template('predict-spam.html')

@app.route('/make-prediction', methods = ['POST'])
def handle_prediction():
    text = request.form['text']
    #text = 'URGENT! You have won a 1 week FREE membership in our √•¬£100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18'
    df = pd.read_csv('./spam_clean.csv')

    tfidf = TfidfVectorizer()

    X = tfidf.fit_transform(df.text)
    y = df.label

    lm = LogisticRegression(solver='saga').fit(X, y)
    
    prediction = lm.predict(tfidf.transform([text]))[0]

    if prediction == 'ham':
        prediction = 'hammy'
    else:
        prediction = 'spammy'

    #type(prediction)

    return render_template('prediction-result.html', prediction = prediction)
