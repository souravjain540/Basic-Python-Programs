import random
number=random.randint(1,100)


def guessNUmber(number, num , level):

    while level!=1:
        if(num>number):
            print("Too High")
        else:print("Too Low")
        level-=1
        print(f"YOU have {level} attemps left")
        num = int(input("Guess the number : "))

    if(num==number):print(f"YOU GUESSED IT CORRECT IT WAS {num}")
    else:print(f"YOU GUESSED IT WRONG IT WAS {number}")

print("choose the level of game 'hard' or 'easy'")
level = input().lower()

while True:


    if(level!="hard" and level!="easy"):
        print("Invalid Choice")
    else:break

    print("choose the level of game 'hard' or 'easy'")
    level = input().lower()

print("I am thinking of a number betwen 1-100. \n ")
num = int(input("Guess the number : "))

if level == "hard":
    guessNUmber(number, num, 5)
elif level == "easy:":
    guessNUmber(number, num, 10)
