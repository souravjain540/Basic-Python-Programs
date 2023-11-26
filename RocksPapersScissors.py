a=1
while  a:
    print("Enter Player_1 name: " )
    Player_1=input()
    print("Enter Player_2 name: " )
    Player_2=input()
    print("=="*30)
    print("# "*5+Player_1+"'s turn  "+" #"*5)
    print("Enter your option "+Player_1+" ::")
    print("R=Rock / P=Paper // S=Scissors")
    Player_1_choice=input()
    print("# "*5+Player_2+"'s turn  "+" #"*5)
    print("Enter your option "+Player_2+" ::")
    print("R=Rock / P=Paper // S=Scissors")
    Player_2_choice=input()
    print("=="*30)
    if Player_1_choice=="R":
        if Player_2_choice=="R":
            print("DRAW")
        elif Player_2_choice=="P":
            print(Player_2 +" WINS")
        elif Player_2_choice=="S":
            print(Player_1 +" WINS")
    elif Player_1_choice=="P":
        if Player_2_choice=="P":
            print("DRAW")
        elif Player_2_choice=="R":
            print(Player_1 + " WINS")
        elif Player_2_choice=="S":
            print(Player_2+ " WINS")
    elif Player_1_choice=="S":
        if Player_2_choice=="S":
            print("DRAW")
        elif Player_2_choice=="P":
            print(Player_1+ " WINS")
        elif Player_2_choice=="R":
            print(Player_2+ " WINS")
    print("::"*30)
    print("Enter 1 to Play-Again")
    print("Enter 0 to Exit")
    a=int(input())


