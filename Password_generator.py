#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def easy_pass(nr_letters,nr_symbols,nr_numbers):
  random_letters = ""
  for i in range(0,nr_letters):
    random_letter = r.choice(letters)
    random_letters += random_letter

  random_symbols = ""
  for i in range(0,nr_symbols):
    random_symbol = r.choice(symbols)
    random_symbols += random_symbol

  random_numbers = ""
  for i in range(0,nr_numbers):
    random_number = r.choice(numbers)
    random_numbers += random_number

  #Easy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  final_password = random_letters + random_symbols + random_numbers
  print(f"Here is your easy password : {final_password}")

def hard_pass(nr_letters,nr_symbols,nr_numbers):
  random_letters = []
  for i in range(0,nr_letters):
    random_letter = r.choice(letters)
    random_letters.append(random_letter)

  random_symbols = []
  for i in range(0,nr_symbols):
    random_symbol = r.choice(symbols)
    random_symbols.append(random_symbol)

  random_numbers = []
  for i in range(0,nr_numbers):
    random_number = r.choice(numbers)
    random_numbers.append(random_number)

  final_password_list = random_letters + random_symbols + random_numbers
  r.shuffle(final_password_list)


  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  final_pass_in_str = ""
  for char in final_password_list:
    final_pass_in_str += char
  print(f"Here is your hard password : {final_pass_in_str}")


def password_generator():
  print("Welcome to the PyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  
  print()
  easy_pass(nr_letters,nr_symbols,nr_numbers)
  print()
  hard_pass(nr_letters,nr_symbols,nr_numbers)


def main():
  password_generator()


if __name__ == '__main__':
  main()
