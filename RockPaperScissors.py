
import random
from termcolor import colored

try:

        def rock_paper_scissors():
            print("Welcome to Rock, Paper, Scissors Game!")

            score = 0

            while True:
        
                choice = ["rock", "paper", "scissor"]
                player_choice = input("Enter your choice (rock, paper and scissor) or 'Q' to quite: ").lower().strip() 


                if player_choice.lower().strip() == "q":
                    print("Thanks for palying.")
                    break
            

                if player_choice not in choice:
                    print("Invalid input!")
                    continue  
                
                computer_choice = random.choice(choice)
                print(f"Computer choose {computer_choice}")

                if player_choice == computer_choice:
                    print(colored("It's a tie!", "blue"))
                elif  (player_choice == "rock" and computer_choice == "scissor") or \
                    (player_choice == "paper" and computer_choice == "rock") or \
                    (player_choice == "scissor" and computer_choice == "paper"):
                    score += 1
                    print(colored("You win!", "green"))
                   
                else:
                  print(colored("You lose!", "red"))

                print(colored(f"Your score: {score}", "light_yellow"))

except:
     print("")

(rock_paper_scissors())

            
        


        