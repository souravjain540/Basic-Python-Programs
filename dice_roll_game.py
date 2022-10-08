import random
min_val = 1
max_val = 6

def roll(input):
    if input == "yes" or input == "Yes" or input == "y" or input == "Y":
        print("Dices rolling...")
        print("The values are :")
        print(random.randint(min_val, max_val))
        print(random.randint(min_val, max_val))
    else:
        print("Thank you for playing!")


roll_again = input("Do you want to roll the Dices?")
roll(roll_again);