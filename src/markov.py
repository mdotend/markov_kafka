from string import punctuation
from collections import defaultdict
from random import choice


def remove_punctuations(pText):
    return pText.translate(str.maketrans('','', punctuation + "»«"))

def remove_newlines(pText):
    newlinesTrans = {
        "\n": " ", #replace newline with space
        "\r": "", #remove return char
    }
    return pText.translate(str.maketrans(newlinesTrans))

def unifyText(pText):
    woPuntuation = remove_punctuations(pText)
    woNewlines = remove_newlines(woPuntuation)
    return woNewlines

def model(pText):
    '''
    This function will take a block of text as the input and map each word in the text to a key where the
    values associated to that key are the words which proceed it
    args:
        text (String) : The string of text you wish to train your markov model around
    example:
        text = 'hello my name is V hello my name is G hello my current name is F world today is a good day'
        markov_model(text)
        >> {'F': ['world'],
            'G': ['hello'],
            'V': ['hello'],
            'a': ['good'],
            'current': ['name'],
            'good': ['day'],
            'hello': ['my', 'my', 'my'],
            'is': ['V', 'G', 'F', 'a'],
            'my': ['name', 'name', 'current'],
            'name': ['is', 'is', 'is'],
            'today': ['is'],
            'world': ['today']}
    '''

    # split the input text into individual words seperated by spaces
    words = pText.split(' ')

    markov_dict = defaultdict(list)

    # create list of all word pairs
    for current_word, next_word in zip(words[0:-1], words[1:]):
        markov_dict[current_word].append(next_word)

    markov_dict = dict(markov_dict)
    print('Successfully Trained')
    return markov_dict
    
def predict_words(chain, first_word, number_of_words=5):
    '''
    Given the input result from the markov_model function and the nunmber of words, this function will allow you to predict the next word
    in the sequence
    
    args:
        chain (Dictionary) : The result of the markov_model function
        first_word (String) : The word you want to start your prediction from, note this word must be available in chain
        number_of_words (Integer) : The number of words you want to predict
    
    example:
        chain = markov_model(text)
        generate_sentence(chain, first_word = 'do', number_of_words = 3)
        >> Do not fail.
    '''
    
    if first_word in list(chain.keys()):
        word1 = str(first_word)
        
        predictions = word1.capitalize()

        # Generate the second word from the value list. Set the new word as the first word. Repeat.
        for i in range(number_of_words-1):
            word2 = choice(chain[word1])
            word1 = word2
            predictions += ' ' + word2

        # End it with a period
        predictions += '.'
        return predictions
    else:
        return "Word not in corpus"

 