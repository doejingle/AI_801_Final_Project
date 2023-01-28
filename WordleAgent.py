class WordleAgent():
    def __init(self):
        pass
    
    def guess_word(self,
                   words_df,
                   word_column,
                   previous_guesses=[],
                   not_in_word=[],
                   letter_1='',
                   letter_2='',
                   letter_3='',
                   letter_4='',
                   letter_5='',
                   letter_1_not=[],
                   letter_2_not=[],
                   letter_3_not=[],
                   letter_4_not=[],
                   letter_5_not=[],
                   contains_letters=[]
                  ):
            
        likely_words = words_df
        
        likely_words = likely_words[~likely_words[word_column].isin(previous_guesses)]
        
        if len(list(set(not_in_word))) > 0:
            for letter in list(set(not_in_word)):
                likely_words = likely_words[~likely_words[word_column].str.contains(letter)]
        else:
            pass
        
        if len(list(set(contains_letters))) > 0:
            for letter in list(set(contains_letters)):
                likely_words = likely_words[words_df[word_column].str.contains(letter)]
        else:
            pass
        
        # letter 1 equal to
        if letter_1 != '':
            likely_words = likely_words[likely_words['letter_1'] == letter_1]
        else:
            pass
        
        # letter 1 not equal to
        if len(letter_1_not) > 0:
            for letter in list(set(letter_1_not)):
                likely_words = likely_words[likely_words['letter_1'] != letter]
        else:
            pass
        
        # letter 2 equal to
        if letter_2 != '':
            likely_words = likely_words[likely_words['letter_2'] == letter_2]
        else:
            pass
        
        # letter 2 not equal to
        if len(letter_2_not) > 0:
            for letter in list(set(letter_2_not)):
                likely_words = likely_words[likely_words['letter_2'] != letter]
        else:
            pass
        
        # letter 3 equal to
        if letter_3 != '':
            likely_words = likely_words[likely_words['letter_3'] == letter_3]
        else:
            pass
        
        # letter 3 not equal to
        if len(letter_3_not) > 0:
            for letter in list(set(letter_3_not)):
                likely_words = likely_words[likely_words['letter_3'] != letter]
        else:
            pass
        
        # letter 4 equal to
        if letter_4 != '':
            likely_words = likely_words[likely_words['letter_4'] == letter_4]
        else:
            pass
        
        # letter 4 not equal to
        if len(letter_4_not) > 0:
            for letter in list(set(letter_4_not)):
                likely_words = likely_words[likely_words['letter_4'] != letter]
        else:
            pass
        
        # letter 5 equal to
        if letter_5 != '':
            likely_words = likely_words[likely_words['letter_5'] == letter_5]
        else:
            pass
        
        # letter 5 not equal to
        if len(letter_5_not) > 0:
            for letter in list(set(letter_5_not)):
                likely_words = likely_words[likely_words['letter_5'] != letter]
        else:
            pass
        
        try:
            guessed_word = likely_words[word_column].values[0]
        except:
            print('No words meet this/these criteria')
            
        print(f'You should guess {guessed_word}')
        
        return guessed_word
    
    def guess_word_automated(self,
                   words_df,
                   word_column,
                   previous_guesses=[],
                   not_in_word=[],
                   letter_1='',
                   letter_2='',
                   letter_3='',
                   letter_4='',
                   letter_5='',
                   letter_1_not=[],
                   letter_2_not=[],
                   letter_3_not=[],
                   letter_4_not=[],
                   letter_5_not=[],
                   contains_letters=[]
                  ):
            
        likely_words = words_df
        
        likely_words = likely_words[~likely_words[word_column].isin(previous_guesses)]
        
        if len(list(set(not_in_word))) > 0:
            for letter in list(set(not_in_word)):
                likely_words = likely_words[~likely_words[word_column].str.contains(letter)]
        else:
            pass
        
        if len(list(set(contains_letters))) > 0:
            for letter in list(set(contains_letters)):
                likely_words = likely_words[words_df[word_column].str.contains(letter)]
        else:
            pass
        
        # letter 1 equal to
        if letter_1 != '':
            likely_words = likely_words[likely_words['letter_1'] == letter_1]
        else:
            pass
        
        # letter 1 not equal to
        if len(letter_1_not) > 0:
            for letter in list(set(letter_1_not)):
                likely_words = likely_words[likely_words['letter_1'] != letter]
        else:
            pass
        
        # letter 2 equal to
        if letter_2 != '':
            likely_words = likely_words[likely_words['letter_2'] == letter_2]
        else:
            pass
        
        # letter 2 not equal to
        if len(letter_2_not) > 0:
            for letter in list(set(letter_2_not)):
                likely_words = likely_words[likely_words['letter_2'] != letter]
        else:
            pass
        
        # letter 3 equal to
        if letter_3 != '':
            likely_words = likely_words[likely_words['letter_3'] == letter_3]
        else:
            pass
        
        # letter 3 not equal to
        if len(letter_3_not) > 0:
            for letter in list(set(letter_3_not)):
                likely_words = likely_words[likely_words['letter_3'] != letter]
        else:
            pass
        
        # letter 4 equal to
        if letter_4 != '':
            likely_words = likely_words[likely_words['letter_4'] == letter_4]
        else:
            pass
        
        # letter 4 not equal to
        if len(letter_4_not) > 0:
            for letter in list(set(letter_4_not)):
                likely_words = likely_words[likely_words['letter_4'] != letter]
        else:
            pass
        
        # letter 5 equal to
        if letter_5 != '':
            likely_words = likely_words[likely_words['letter_5'] == letter_5]
        else:
            pass
        
        # letter 5 not equal to
        if len(letter_5_not) > 0:
            for letter in list(set(letter_5_not)):
                likely_words = likely_words[likely_words['letter_5'] != letter]
        else:
            pass
        
        try:
            guessed_word = likely_words[word_column].values[0]
        except:
            pass
            
#        print(f'You should guess {guessed_word}')
        
        return guessed_word