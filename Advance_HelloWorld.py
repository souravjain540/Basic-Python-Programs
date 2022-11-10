from random import randint
from time import sleep

words = "Hello, World!"  # String of words to print
guess = ""  # String of program's guess

# Print each character in words with a random delay
for i in range(len(words)):
    while True:  # Loop until program guesses correctly
        rand_char = chr(randint(32, 127))
        print(guess, end='')
        print(rand_char)
        sleep(0.02)  # Delay to make program slower
        if rand_char == words[i]:
            guess += rand_char
            break