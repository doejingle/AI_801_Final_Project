import pandas as pd
import plotly.express as px
from tqdm import tqdm
from Wordle import Wordle


def gameplay_iteration(games_per_iteration=10,iterations=10):
    final_results = []
    all_results = []
    all_guesses = []
    all_true_words = []
    for i in tqdm(range(iterations)):
        win = [0]
        for i in range(games_per_iteration):
            wordle = Wordle()
            prev,true,result,final_result,guesses = wordle.play_automated()
            all_results.append(final_result)
            all_guesses.append(guesses)
            all_true_words.append(true)
            win.append(win[i] + final_result)
        final_results.append(win[-1])
    results_df = pd.DataFrame(final_results,columns=['wins'])
    detailed_results_df = pd.DataFrame(all_results,columns=['result'])
    detailed_results_df['guesses'] = all_guesses
    detailed_results_df['true_word'] = all_true_words
    detailed_wins_df = detailed_results_df[detailed_results_df['result'] == True]
    histogram_wins_per_iteration = px.histogram(results_df,
                                                x='wins',
                                                marginal='box',
                                                title='Histogram - Wins per iteration')
    histogram_guesses_per_win = px.histogram(detailed_results_df,
                                             x='guesses',
                                             marginal='box',
                                             title='Histogram - Guesses per win')
    return results_df,detailed_results_df,histogram_wins_per_iteration,histogram_guesses_per_win

# play one game at a time
wordle = Wordle()
prev,true,result = wordle.play()

# play multiple iterations
(results_df,
 detailed_results_df,
 histogram_wins_per_iteration,
 histogram_guesses_per_win
) = gameplay_iteration(games_per_iteration=100,
                       iterations=100
                      )
histogram_wins_per_iteration.show()
histogram_guesses_per_win.show()

results_df,histogram = gameplay_iteration(games_per_iteration=20,
                                          iterations=1000)
histogram

# TODO
## add weighting for unique letters (see if it even helps)
## find wordle word database