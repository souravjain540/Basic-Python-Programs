#!/usr/bin/env python3

"""
Convert a hex digit to decimal

Version: 1.0
Python 3.11+
Date created: November 17th, 2023
Date modified: -
"""

import sys


def hex_to_dec(hex_digit: str):
    if hex_digit <= "F" and hex_digit >= "A":
        # The ord() function returns the ASCII code for
        # the given character.
        value = ord(hex_digit) - ord("A") + 10
        print(f"The decimal value for {hex_digit} is {value}.")
    elif hex_digit.isdigit():
        print(f"The decimal value for {hex_digit} is {hex_digit}.")
    else:
        print("The input value is invalid!")


def main():
    hex_digit = input("Enter a hex digit: ").upper()

    if len(hex_digit) != 1:
        sys.exit("You entered more than one digit!")

    hex_to_dec(hex_digit)


if __name__ == "__main__":
    main()
