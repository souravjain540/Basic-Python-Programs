import random
import string

n = int(input("Enter the length of password : "))
password_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(password_characters) for i in range(n))
print("Password = {}".format(password))
