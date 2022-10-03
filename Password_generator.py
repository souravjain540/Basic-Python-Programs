#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letters = ""
for i in range(0,nr_letters):
  random_letter = r.choice(letters)
  random_letters += random_letter

# print(random_letters)

random_symbols = ""
for i in range(0,nr_symbols):
  random_symbol = r.choice(symbols)
  random_symbols += random_symbol

# print(random_symbols)

random_numbers = ""
for i in range(0,nr_numbers):
  random_number = r.choice(numbers)
  random_numbers += random_number

# print(random_numbers)

final_password = random_letters + random_symbols + random_numbers
print(f"Here is your easy password : {final_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_letters = []
for i in range(0,nr_letters):
  random_letter = r.choice(letters)
  random_letters.append(random_letter)

# print(random_letters)

random_symbols = []
for i in range(0,nr_symbols):
  random_symbol = r.choice(symbols)
  random_symbols.append(random_symbol)

# print(random_symbols)

random_numbers = []
for i in range(0,nr_numbers):
  random_number = r.choice(numbers)
  random_numbers.append(random_number)

# print(random_numbers)

final_password_list = random_letters + random_symbols + random_numbers
r.shuffle(final_password_list)

final_pass_in_str = ""
for char in final_password_list:
  final_pass_in_str += char
print(f"Here is your difficult password : {final_pass_in_str}")
