import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list =[]
for i in range(0,nr_letters):
  rand1 = random.randint(0,51)
  password_list.append(letters[rand1])
for i in range(0,nr_symbols):
  rand2 = random.randint(0,8)
  password_list.append(symbols[rand2])
for i in range(0,nr_numbers):
  rand3 = random.randint(0,9)
  password_list.append(numbers[rand3])
random.shuffle(password_list)
password2 = ""
for i in password_list:
  password2+=i
print(f"Your password is {password2}")