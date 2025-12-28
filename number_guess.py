import random

number = random.randint(1, 10)
tries = 3

while tries > 0:
    try:
        guess = int(input(f"Guess the number (1-10). Attempts left: {tries}: "))
    except ValueError:
        print("Invalid input. Enter an integer.")
        continue

    if guess == number:
        print("Correct. You win.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    tries -= 1

if tries == 0:
    print(f"You lose. The number was {number}.")
