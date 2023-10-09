"""This file has the function which reverses real integer."""
'''Reverse of a user input number with best time complexity'''

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

try:
    num = int(input("Enter a number: "))
    reversed_num = reverse_number(num)
    print("Reverse of", num, "is", reversed_num)
except ValueError:
    print("Invalid input. Please enter a valid number.")
