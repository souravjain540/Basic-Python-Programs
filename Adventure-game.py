def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the edge of a dark forest.")
    print("Can you find the treasure hidden within?")

    first_choice = input("Do you step into the forest? (yes/no): ").lower()
    
    if first_choice == "yes":
        print("\nYou bravely step into the forest.")
        
        second_choice = input("You come to a fork in the road. Do you go left or right? (left/right): ").lower()

        if second_choice == "left":
            print("\nYou find a treasure chest! You win!")
        elif second_choice == "right":
            print("\nA wild bear appears and chases you out of the forest! You lose!")
        else:
            print("\nInvalid choice. Game over.")
    elif first_choice == "no":
        print("\nYou decide not to enter the forest. Maybe next time!")
    else:
        print("\nInvalid choice. Game over.")

if __name__ == "__main__":
    adventure_game()
