from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from utils import initialize_guesses, clear_guesses, store_guess

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():

    test_word = 'CRANE'

    # Initialize the guesses in the session
    session = initialize_guesses()

    # Clear guesses if button pushed
    if request.method == 'POST' and request.form['guess']=="Clear Guesses":
        session = clear_guesses()
    else:
        # Store user guesses in the session
        if request.method == 'POST':
            if len(request.form['guess'])==5:
                session = store_guess(request.form['guess'].upper())
            else:
                flash("Please guess a 5-Letter word", category="error")

    return render_template('home.html', session=session, test_word=test_word)

