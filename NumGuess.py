def number_guess():
    import random
    print("Welcome To number Guessing game!!!!")
    print("Computer is picking a number between 1 and 10")
    n=random.randint(1, 10)
    print("Computer has selected a number")
    a=3
    while a!=0:
        print("You have ",a," guesses")
        m=int(input("Place Your Guess: "))
        if 10>abs(m-n)>5:
            print("You are not even close lol")
            a-=1
        elif abs(m-n)in range (3,6):
            print("Get a little closer")
            a-=1
        elif 1<abs(m-n)<3:
            print("You are very close")
            a-=1
        elif abs(m-n)==1:
            print("You are just one away")
            a-=1
        elif abs(m-n)>=10:
            print("Invalid Input")
            a-=1
        elif int(m)==int(n):
            print ("You got it!!!! Good job")
            break
    if a==0:
        print("You're all out guesses! Better luck next time!")
        print("The number selected by Computer was ",n)
number_guess()