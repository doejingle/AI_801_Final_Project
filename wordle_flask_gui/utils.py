from flask import session

def initialize_guesses():
    for i in range(1,7):
        if f'guess{i}' not in session:
            session[f'guess{i}'] = ''
    return session   

def clear_guesses():
    for i in range(1,7):
        session[f'guess{i}'] = ''
    return session   

def store_guess(guess):
    if session["guess1"] == '':
        session["guess1"] = guess
    elif session["guess2"] == '':
        session["guess2"] = guess
    elif session["guess3"] == '':
        session["guess3"] = guess
    elif session["guess4"] == '':
        session["guess4"] = guess
    elif session["guess5"] == '':
        session["guess5"] = guess
    elif session["guess6"] == '':
        session["guess6"] = guess
    else:
        pass
    return session