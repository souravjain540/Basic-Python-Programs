import random

randomInteger=random.randint(0,2)
userInput=int(input("What do you choose ? Type 0 for Rock,1 for Paper or 2 for Scissors\n"))
if(userInput!=0 and userInput!=1 and userInput!=2):
    print("Wrong choise")
    exit()

if(userInput==randomInteger):
    print("DRAW!!!")
elif (userInput==randomInteger-1 or (userInput==2 and randomInteger==0)):
    print("Computer Won")
elif (randomInteger==userInput-1 or (randomInteger==2 and userInput==0)):
    print("YOU WON!!!")
print(userInput)
print(f"computer choose {randomInteger}")