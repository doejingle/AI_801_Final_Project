from WordleAgent import WordleAgent
from WordleLetterScores import english_words_5_characters_df, english_words_5_characters_letters_df

class Wordle():
    def __init__(self):
        pass
    
    def generate_word(self,words_df,column):
        word = words_df[column].sample(1).values[0]
        return word
    
    def assess_word(self,guessed_word,true_word):
        result = []
#        print(f'Guessed word: {guessed_word}')
#        print(f'True word: {true_word}')
        if guessed_word == true_word:
            result = ['G','G','G','G','G']
#            print('Words are the same - you win')
        else:
            for i,j in zip(guessed_word,true_word):
                if i == j:
                    result.append('G')
                elif i in true_word:
                    result.append('Y')
                else:
                    result.append('-')
        return result
        
    def play(self):
        true_word = self.generate_word(english_words_5_characters_df,column='word')
        previous_guesses = []
        not_in_word=[]
        letter_1=''
        letter_2=''
        letter_3=''
        letter_4=''
        letter_5=''
        letter_1_not=[]
        letter_2_not=[]
        letter_3_not=[]
        letter_4_not=[]
        letter_5_not=[]
        contains_letters=[]
        for i in range(1,7):
            print(f'Attempt #{i}')
            if i == 1:
                first_guess = (WordleAgent().guess_word(words_df=english_words_5_characters_letters_df,
                                           word_column='word'
                                          )
                              )
            guessed_word = input('Make your guess: ')
            guessed_word
            previous_guesses.append(guessed_word)
            result = self.assess_word(guessed_word,true_word)
            print(result)
            if i == 6 and result != ['G','G','G','G','G']:
                print('Incorrect guess - you lose')
                print(f'The correct answer was {true_word}')
            elif result == ['G','G','G','G','G']:
                print('Correct - you win')
                break
            else:
                for a,b,c in zip(previous_guesses[-1],result,range(1,6)):
                    if c == 1:
                        if b == 'G':
                            letter_1 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_1_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 2:
                        if b == 'G':
                            letter_2 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_2_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 3:
                        if b == 'G':
                            letter_3 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_3_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 4:
                        if b == 'G':
                            letter_4 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_4_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 5:
                        if b == 'G':
                            letter_5 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_5_not.append(a)
                        else:
                            not_in_word.append(a)
                
                next_guess = (WordleAgent()
                              .guess_word(words_df=english_words_5_characters_letters_df,
                                          word_column='word',
                                          previous_guesses=previous_guesses,
                                          not_in_word=not_in_word,
                                          contains_letters=contains_letters,
                                          letter_1=letter_1,
                                          letter_2=letter_2,
                                          letter_3=letter_3,
                                          letter_4=letter_4,
                                          letter_5=letter_5,
                                          letter_1_not=letter_1_not,
                                          letter_2_not=letter_2_not,
                                          letter_3_not=letter_3_not,
                                          letter_4_not=letter_4_not,
                                          letter_5_not=letter_5_not
                                         )
                             )

            print('')
        return previous_guesses,true_word,result
    
    def play_automated(self):
        true_word = self.generate_word(english_words_5_characters_df,column='word')
        previous_guesses = []
        not_in_word=[]
        letter_1=''
        letter_2=''
        letter_3=''
        letter_4=''
        letter_5=''
        letter_1_not=[]
        letter_2_not=[]
        letter_3_not=[]
        letter_4_not=[]
        letter_5_not=[]
        contains_letters=[]
        for i in range(1,7):
            if i == 1:
                next_guess = (WordleAgent()
                               .guess_word_automated(words_df=english_words_5_characters_letters_df,
                                                     word_column='word'
                                                    )
                              )
                guessed_word = next_guess
            
            guessed_word = next_guess
            previous_guesses.append(guessed_word)
            result = self.assess_word(guessed_word,true_word)
            
            if i == 6 and result != ['G','G','G','G','G']:
                final_result = False
                guesses = i
            elif result == ['G','G','G','G','G']:
                final_result = True
                guesses = i
                break
            else:
                for a,b,c in zip(previous_guesses[-1],result,range(1,6)):
                    if c == 1:
                        if b == 'G':
                            letter_1 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_1_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 2:
                        if b == 'G':
                            letter_2 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_2_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 3:
                        if b == 'G':
                            letter_3 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_3_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 4:
                        if b == 'G':
                            letter_4 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_4_not.append(a)
                        else:
                            not_in_word.append(a)
                    if c == 5:
                        if b == 'G':
                            letter_5 = a
                        elif b == 'Y':
                            contains_letters.append(a)
                            letter_5_not.append(a)
                        else:
                            not_in_word.append(a)
                
                next_guess = (WordleAgent()
                              .guess_word_automated(words_df=english_words_5_characters_letters_df,
                                                    word_column='word',
                                                    previous_guesses=previous_guesses,
                                                    not_in_word=not_in_word,
                                                    contains_letters=contains_letters,
                                                    letter_1=letter_1,
                                                    letter_2=letter_2,
                                                    letter_3=letter_3,
                                                    letter_4=letter_4,
                                                    letter_5=letter_5,
                                                    letter_1_not=letter_1_not,
                                                    letter_2_not=letter_2_not,
                                                    letter_3_not=letter_3_not,
                                                    letter_4_not=letter_4_not,
                                                    letter_5_not=letter_5_not
                                                   )
                             )

        return previous_guesses,true_word,result,final_result,guesses