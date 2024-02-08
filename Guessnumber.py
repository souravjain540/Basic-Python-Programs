import random

def generate_random_number(min_value, max_value):

    if min_value >= max_value:
        raise ValueError("Minimum value must be less than maximum value.")
    return random.randint(min_value, max_value)

def validate_difficulty_level(level):

    valid_levels = ["hard", "easy"]
    if level.lower() not in valid_levels:
        raise ValueError("Invalid difficulty level. Choose 'hard' or 'easy'.")
    return level.lower()

def guess_number(random_number, level):

    attempts = 5 if level == "hard" else 10

    while attempts > 0:
        try:
            guess = int(input(f"Guess the number between 1 and 100 ({attempts} attempts left): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < 1 or guess > 100:
            print("Guess must be between 1 and 100.")
            continue

        if guess == random_number:
            print("You guessed it correctly!")
            return
        elif guess < random_number:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1

    print(f"You ran out of attempts. The number was {random_number}.")

def main():

    try:
        min_value = 1
        max_value = 100
        random_number = generate_random_number(min_value, max_value)

        level = validate_difficulty_level(input("Choose difficulty level ('hard' or 'easy'): "))
        guess_number(random_number, level)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
