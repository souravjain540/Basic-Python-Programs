def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    Parameters:
    - num (int): The integer to be converted. Should be a positive integer.

    Returns:
    - str: The Roman numeral representation of the input integer.
    """

    if num <= 0:
        raise ValueError("Input must be a positive integer")

    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    # Iterate through the Roman numeral symbols in descending order of value
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        # Repeat the symbol while the remaining number is greater than or equal to the current value
        while num >= value:
            result += symbol
            num -= value  # Subtract the value from the remaining number

    return result

# Example usage:
try:
    # Get user input for a positive integer
    number = int(input("Enter a positive integer: "))
    # Convert the integer to a Roman numeral
    roman_numeral = int_to_roman(number)
    # Display the result
    print(f"The Roman numeral representation of {number} is: {roman_numeral}")
except ValueError as ve:
    print(f"Error: {ve}")
