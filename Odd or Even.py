#I made this programm because it was in my first job interview as a programmer

#Getting user input
while True:
    try:
        user = int(input("Give me a Number range : 0 - "))
        user += 1
        break
    except ValueError:
        print("Pls Enter a Number")

#Getting every number from the input number range and printing if its odd or even
for i in range(int(user)):
    if i % 2 <= 0:
        print(str(i) + " Even")
    elif i % 2 > 0:
        print(str(i) + " Odd")
    else:
        print("Error")