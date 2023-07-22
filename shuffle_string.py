import random


def shuffle(word):
    return ''.join(random.sample(word, len(word)))


word = input("Type a word: ")

print(f"The shuffle of the word '{word}' is '{shuffle(word)}'")
