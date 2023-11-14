'''
A pangram is a sentence that uses all the letters in the alphabet

'''

import string
# this function tests if a string is a pangram or not


def isPangram(sentence):
    # get all characters of the alphabet in a set
    sentenceSet = set(sentence.lower())
    # get all character of the input sentence in another set
    allChars = set(string.ascii_lowercase)
    # for each letter of the sentence check if it is in the allChars set
    for letter in sentenceSet:
        if letter in allChars:
            # if it is part of the set remove it
            allChars.remove(letter)
    # if allChars is empty it is a pangram,else it isnt
    if allChars:
        return False
    else:
        return True


print(isPangram("The five boxing wizards jump quickly"))
print(isPangram("I am an Indian"))
