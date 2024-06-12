# A series of toy functions that change the capitalization of a string in interesting ways.
# Possibly useful as examples of ternary operators in Python.

import random
import string
from nltk.tag import pos_tag # need to run nltk.download('averaged_perceptron_tagger') 

def randomCaps(text):
    """
    Randomizes capitalization of a text.
    """
    if(type(text) != str):
        raise ValueError("This function can only convert strings!")
    text = list(text)
    for i in range(len(text)):
        text[i] = text[i].upper() if random.random() > 0.5 else text[i].lower()
    return ''.join(text)

def alternatingCaps(text):
    """
    Alternates capitalization of a text.
    """
    if(type(text) != str):
        raise ValueError("This function can only convert strings!")
    text = list(text)
    for i in range(len(text)):
        text[i] = text[i].lower() if i % 2 == 0 else text[i].upper()
    return ''.join(text)

def switchCaps(text):
    """
    Alternates capitalization, with minor randomness for additional interest.

    Idea from Al Sweitgart's "The Big Book of Small Python Projects" ("spongecase"), but code is my own.
    """
    if(type(text) != str):
        raise ValueError("This function can only convert strings!")
    text = list(text)
    for i in range(len(text)):
        if(random.random() > 0.9):
            text[i] = text[i].upper() if i % 2 == 0 else text[i].lower()
        else:
            text[i] = text[i].lower() if i % 2 == 0 else text[i].upper()
    return ''.join(text)

def nameCaps(text):
    """
    Capitalizes the full word of all proper nouns in correctly-capitalized text.

    May require additional downloads to nltk library to work.
        nltk.download('averaged_perceptron_tagger')
    """
    if(type(text) != str):
        raise ValueError("This function can only convert strings!")
    tagged_text = pos_tag(text.split()) # [ (word, part_of_speech_tag), ...]
    text = [list(tup) for tup in tagged_text] # [ [word, POS_tag], ...]
    text = [pair[0].upper() if pair[1] == 'NNP' else pair[0] for pair in text] # if proper noun, capitalize word
    return ' '.join(text)

def camelCaps(text):
    """
    Changes a string to one-word no-punctuation camel case.
    """
    if(type(text) != str):
        raise ValueError("This function can only convert strings!")
    text = text.translate(str.maketrans('','',string.punctuation)) # remove punctuation
    text = text.split()
    text[0] = text[0].lower()
    for i in range(1,len(text)):
        text[i] = text[i].title()
    return ''.join(text)


if __name__ == '__main__':
    text = input("Input a string to change its capitalization: ")
    print("Random:", randomCaps(text))
    print("Alternating:", alternatingCaps(text))
    print("Switch:", switchCaps(text))
    print("Capitalized names:", nameCaps(text))
    print("Camel case:", camelCaps(text))
    
    