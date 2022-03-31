from flask import Flask, render_template, session, redirect, request
from random import *
app = Flask (__name__)
app.secret_key = 'super secure'

@app.route('/')
def index():
    session['random'] = randint(1,100)
    session['counter'] = 0
    print(session['random'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if session['counter'] < 4:
        if guess == session['random']:
            session['counter'] += 1
            if session['counter'] == 1:
                guesses = "guess"
            else:
                guesses = "guesses"
            high_low = f"You got it in {session['counter']} {guesses}! The number was {session['random']}."
            return render_template('guess.html', high_low = high_low, color = "green", win = True)
        elif guess > session['random']:
            high_low = "Too High!"
            session['counter'] += 1
            return render_template ('guess.html', high_low = high_low)
        else:
            high_low = "Too Low!"
            session['counter'] += 1
            return render_template('guess.html', high_low = high_low)
    else:
        high_low = "You failed to guess correctly in 5 attempts."
        return render_template('guess.html', high_low = high_low, color = "orange")

@app.route('/leaderboard', methods = ['POST'])
def leaderboard():
    session['leaderboard'] = request.form['name']
    return render_template('leaderboard.html')





app.run(debug = True)