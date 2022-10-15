import random
while True:
 choices = ["rock","paper","scissors"]
 computer = random.choice(choices)
 player = input("rock, paper, scissors?:") .lower()

 while player not in choices:
    player = input("rock, paper, scissors?:") .lower()
    print("invalid choice try again!")
 if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

 elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

 elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")

 elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")

 play_again = input("Play again? (yes/no): ").lower()

 if play_again != "yes":
        break

print("Bye!")
