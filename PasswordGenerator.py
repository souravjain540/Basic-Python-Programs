#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


no_letters=int(input("How many letters would you like to use in password?\n"))
no_symbols=int(input("How many symbols would you like? \n"))
no_numbers=int(input("How many numbers would you like? \n"))




def easy_version():
    password = ""
    for i in range(no_letters):
        ran=random.randint(0,len(letters))
        password+=letters[ran]
    for i in range(no_numbers):
        ran=random.randint(0,len(numbers))
        password+=str(numbers[ran])
    for i in range(no_symbols):
        ran=random.randint(0,len(symbols))
        password+=str(symbols[ran])
    print(password)

def hard_version():
    password_list=[]
    password=""
    for i in range(no_letters):
        ran=random.randint(0,len(letters)-1)
        password_list+=letters[ran]
    for i in range(no_numbers):
        ran=random.randint(0,len(numbers)-1)
        password_list+=str(numbers[ran])
    for i in range(no_symbols):
        ran=random.randint(0,len(symbols)-1)
        password_list+=str(symbols[ran])

    random.shuffle(password_list)
    for i in password_list:
        password+=i

    print(password)


hard_version()


