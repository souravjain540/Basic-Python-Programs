"""
palindrome_number.py
Simple beginner program to check whether an integer is a palindrome.

Usage:
  python3 palindrome_number.py         # interactive input
  python3 palindrome_number.py 121     # runs for the given number (optional argument)
"""

import sys

def is_palindrome_number(n: int) -> bool:
    """
    Return True if integer n is a palindrome (reads same forwards and backwards).

    Works for non-negative integers. Example: 121 -> True, 123 -> False.
    """
    if n < 0:
        return False  # negative numbers have a leading '-' so we treat them as not palindrome
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num

def main():
    # Allow optional command-line argument: python3 palindrome_number.py 121
    if len(sys.argv) > 1:
        try:
            value = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer.")
            return
    else:
        # Interactive input
        try:
            value = int(input("Enter an integer to check palindrome: ").strip())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

    if is_palindrome_number(value):
        print(f"{value} is a palindrome number ✅")
    else:
        print(f"{value} is NOT a palindrome number ❌")

if __name__ == "__main__":
    main()