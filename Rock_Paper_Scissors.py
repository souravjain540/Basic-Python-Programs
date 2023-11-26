import random

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {player_choice}. Computer chose {computer_choice}.")
    print(determine_winner(player_choice, computer_choice))

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
