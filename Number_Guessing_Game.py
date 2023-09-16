import random
i = 1


def game_core(attempts):
    global i
    random_number = random.randint(lower_limit, upper_limit)
    user_guess = int(input("Enter your guess: "))
    if user_guess == random_number:
        print("You win!")
    else:
        if i == attempts:
            print("You lose!")
            print("Game over!")
        else:
            print(f"You have {attempts-i} attempts left")
            i += 1
            game_core(attempts)


print("Welcome to number guessing game.")
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
mode = input("Which level do you want to play(easy or hard): ").lower()
if mode == "easy":
    print("You have 10 attempts to guess the number.")
    game_core(10)
elif mode == "hard":
    print("You have 5 attempts to guess the number.")
    game_core(5)
