#Program for Game to Guess a number

#Intro Code to be displayed at the beginning of the game
def Intro(): 
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Hi and Welcome to Number Guesser!!!")

    print("In your mind choose any number between 1 and 1000")

    print("When the programme displays a number you have will have three options:")

    print("1.Greater\n2.Smaller\n3.Equal")

    print("Give the correct response and your point will be the number of tries the computer takes to guess your number")

    print("Let's Go Then")

    print("--------------------------------------------------------------------------------------------------------------------")

    Ask()

#Asking the user to start a round
def Ask():

    c=input(("Are you ready to begin [Y/N] "))

    if c=='Y' or c=='y' :
        startgame()

    else:
        Ask()

#Game Code using binary search
def startgame():
    low , high = 1, 1000 
    mid = low + (high-low)//2 #integer division
    score = 1
    while(low<=high):  
        mid = low + (high-low)//2
        print("Choose ",mid," is :\n1. Greater\n2. Smaller\n3. Equal\n than your number")
        Response = int(input())
        
        if(Response==1): #Given number is greater than chossen number. So we limit search region between low and mid-1
            score +=1
            high = mid-1
        elif(Response==2): #Given number is smaller than chossen number. So we limit search region between low+1 and mid
            score += 1
            low = mid+1
        else: #Given number is equal to the chossen number. So we end the game and give the score
            print("Your score is", score) 
            b=int(input("Would you like to :\n1.Play Again\n2.Exit\n"))
            if(b==1):
                Ask()
            else:
                return

Intro()


            








