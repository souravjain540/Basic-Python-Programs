
#  Number guessing 
# This is a number guessing game where you will guess the number from 1-100 

import random
randno = random.randint(1,100)

guesses = 0 
userguess = None

while(userguess!=randno):

    try:
        userguess = int(input('Guess The Number : \n'))
    except:
        print("Enter a valid number.")   # Checks whether the number is valid or not 

    if (randno==userguess):
        print ("Yayy, you gussed the right number! ")

    elif (randno<userguess):
        print("Guess the Smaller number") 
    else:
        print("Guess Greater number")
    
    
    guesses +=1                          # Adding the number of guesses; for the total guesses.


print(f"You guessed the number in {guesses} guesses")

print ("This Project was created by Aayush")
