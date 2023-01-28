import pandas as pd
import numpy as np
import plotly.express as px
import nltk
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

# Just using for print statements
# seperate = "\n*******************************************************\n"

# Used initially to download NLTK words...
# Not needed after initial download
# Takes time to run and usually doesn't update anything so no need to run everytime
# nltk.download('words')

def get_letter_percent(df, letter):
    letter_counts = pd.DataFrame(df[letter].value_counts())
    letter_counts = letter_counts.reset_index()
    letter_counts = letter_counts.rename(columns={letter:'count','index':letter})

    english_words_5_characters_counts = df.shape[0]
    letter_counts[f'{letter}_percent'] = (letter_counts
                                .apply(lambda x: x['count'] / english_words_5_characters_counts,
                                        axis=1
                                        )
                                )
    letter_counts = letter_counts[[letter,f'{letter}_percent']]
    return letter_counts

# Step-02: Create DataFrame of all 5-letter English words using NLTK
english_words = set(nltk.corpus.words.words())
english_words_df = pd.DataFrame(english_words,columns=['word'])
english_words_df['word'] = english_words_df['word'].str.lower()
english_words_df['word_length'] = english_words_df.apply(lambda x: len(x['word']),axis=1)
english_words_5_characters_df = english_words_df[english_words_df['word_length'] == 5]

# Uncomment for debug
# print('5-letter English Words:',english_words_5_characters_df.shape[0])
# print("english_words_5_characters_df.head()")
# print(english_words_5_characters_df.head())
# print(seperate)

# Step-03: Break out each letter in each 5-letter word
english_words_5_characters_letters_df = (english_words_5_characters_df['word']
                                         .str
                                         .split('',expand=True)
                                         .iloc[:,1:6]
                                        )
english_words_5_characters_letters_df['word'] = english_words_5_characters_df['word']
english_words_5_characters_letters_df.columns = ['letter_1',
                                                 'letter_2',
                                                 'letter_3',
                                                 'letter_4',
                                                 'letter_5',
                                                 'word'
                                                ]
# Uncomment for debug
# print("english_words_5_characters_letters_df.head()")
# print(english_words_5_characters_letters_df.head())
# print(seperate)

# Step-04: Calculate frequency of each letter in each position
# Get Letter countes for each letter
letter_counts_collection = {}
for i in range(1,6):
    letter_counts_collection[i] = get_letter_percent(english_words_5_characters_letters_df, f'letter_{i}')
    # Uncomment for debug
    # print(f"letter_counts_collection[{i}].head()")
    # print(letter_counts_collection[i].head())
    # print(seperate)


# Step-05: Merge in letter position weights (percentages) with the 5-letter word DataFrame
for i in range(1,6):
    english_words_5_characters_letters_df = pd.merge(left=english_words_5_characters_letters_df,
                                                    right=letter_counts_collection[i],
                                                    on=f'letter_{i}',
                                                    how='left'
                                                    )
# Uncomment for debug
# print(english_words_5_characters_letters_df)
# print(seperate)

# Step-06: Create word-level scores (weights) using letter weights and normalize 0-1
# Words with high scores have letters that occur frequently in that position
english_words_5_characters_letters_df['score'] = (english_words_5_characters_letters_df['letter_1_percent'] *
                                                  english_words_5_characters_letters_df['letter_2_percent'] *
                                                  english_words_5_characters_letters_df['letter_3_percent'] *
                                                  english_words_5_characters_letters_df['letter_4_percent'] *
                                                  english_words_5_characters_letters_df['letter_5_percent']
                                                 )
top_score = english_words_5_characters_letters_df['score'].max()
english_words_5_characters_letters_df['score'] = (english_words_5_characters_letters_df
                                                  .apply(lambda x:
                                                         x['score'] / top_score,
                                                         axis=1
                                                        )
                                                 )
english_words_5_characters_letters_df = (english_words_5_characters_letters_df
                                         .sort_values(by='score',ascending=False)
                                         .reset_index(drop=True)
                                        )
# Uncomment for Debug
# print(english_words_5_characters_letters_df.head())
# print(seperate)