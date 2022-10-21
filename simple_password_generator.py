
"""
Simple password generator, edit the 'password_length' and run it
"""

import random


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_character = '%&()@#$_-'
password_length = 16

options = {
    1: letters,
    2: numbers,
    3: special_character
}


def generate_password():
    password = ''
    for _ in range(0, password_length):
        num = random.randint(1, len(options))
        password += random.choice(options.get(num))  

    return password


print(f'Your password is: {generate_password()}')
