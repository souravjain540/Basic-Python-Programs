#Picks a number between 1 and 100 and has the user guess until they find the number.

# Importing the random module
import random

def choose_random_num(): #Chooses a random number.
    return random.randint(1,101)


def ask_for_guess(): #Asks user for their guess as a number.
    print('What is your guess?')
    user_guess = input()

    if user_guess == 'Q' or user_guess == 'q': #If the user enters Q then the game is over.
        return (f'The number was {random_num}. Thanks for playing!')
    else: 
        return evaluate_guess(int(user_guess)) #Evaluates the user's guess.


def evaluate_guess(user_guess): #Evaluates the user's guess.
    print (f'You guessed {user_guess}.')

    if random_num == user_guess:
         return('Good job!')
    else:

        if (user_guess > random_num):
            print('Too high!')
        elif (user_guess < random_num):
            print('Too low!')

        print('Try again!')
        return(ask_for_guess())


# Start of program
random_num = choose_random_num() #Chooses a random number.
print('Guess a number between 1 and 10. Press Q to give up.')
print(ask_for_guess()) #Asks user for their guess as a number.