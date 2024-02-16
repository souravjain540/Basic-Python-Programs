import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


def easy_version():
    password_list = random.choices(letters, k=no_letters) + random.choices(numbers, k=no_numbers) + random.choices(symbols, k=no_symbols)
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(password)


def hard_version():
    password_list = random.sample(letters, no_letters) + random.sample(numbers, no_numbers) + random.sample(symbols, no_symbols)
    random.shuffle(password_list)
    password = ''.join(password_list)
    print(password)


no_letters = int(input("How many letters would you like to use in password?\n"))
no_symbols = int(input("How many symbols would you like? \n"))
no_numbers = int(input("How many numbers would you like? \n"))

# Choosing version based on user's input
version = input("Choose the password complexity (easy/hard): ").strip().lower()
if version == "easy":
    easy_version()
elif version == "hard":
    hard_version()
else:
    print("Invalid choice. Please choose either 'easy' or 'hard'.")



