# Function to check if the given number is a valid binary number (only contains '0' or '1')
def is_valid_binary(number):
    return all(char in '01' for char in number)

# Function to check if the given number is a valid decimal number (contains only digits)
def is_valid_decimal(number):
    return number.isdigit()

# Function to check if the given number is a valid hexadecimal number (valid hex characters)
def is_valid_hexadecimal(number):
    try:
        # Try converting the input to an integer with base 16 (hexadecimal)
        int(number, 16)
        return True
    except ValueError:
        return False

# Function to check if the given number is a valid octal number (only digits from 0-7)
def is_valid_octal(number):
    try:
        # Try converting the input to an integer with base 8 (octal)
        int(number, 8)
        return True
    except ValueError:
        return False

# Function to repeatedly prompt the user until a valid number for the specified input type is given
def get_valid_input(input_type):
    while True:  # Loop until valid input is provided
        if input_type == 'binary':
            number = input("Enter a binary number: ")
            if is_valid_binary(number):  # Validate the binary input
                return number  # Return valid binary number
            else:
                print("Invalid binary number. Please enter a valid binary number (only 0 and 1).")
        elif input_type == 'decimal':
            number = input("Enter a decimal number: ")
            if is_valid_decimal(number):  # Validate the decimal input
                return number  # Return valid decimal number
            else:
                print("Invalid decimal number. Please enter a valid decimal number.")
        elif input_type == 'hexadecimal':
            number = input("Enter a hexadecimal number: ")
            if is_valid_hexadecimal(number):  # Validate the hexadecimal input
                return number  # Return valid hexadecimal number
            else:
                print("Invalid hexadecimal number. Please enter a valid hexadecimal number.")
        elif input_type == 'octal':
            number = input("Enter an octal number: ")
            if is_valid_octal(number):  # Validate the octal input
                return number  # Return valid octal number
            else:
                print("Invalid octal number. Please enter a valid octal number.")

# Function to convert the number from the specified input type to other number systems
def convert_number(number, input_type):
    if input_type == 'binary':
        decimal_value = int(number, 2)  # Convert binary to decimal
    elif input_type == 'decimal':
        decimal_value = int(number)  # Already decimal, just convert to int
    elif input_type == 'hexadecimal':
        decimal_value = int(number, 16)  # Convert hexadecimal to decimal
    elif input_type == 'octal':
        decimal_value = int(number, 8)  # Convert octal to decimal

    # Print the number in all formats: Decimal, Binary, Hexadecimal, and Octal
    print(f"Decimal: {decimal_value}")
    print(f"Binary: {bin(decimal_value)[2:]}")  # Convert to binary, strip '0b' prefix
    print(f"Hexadecimal: {hex(decimal_value)[2:].upper()}")  # Convert to hex, strip '0x' and convert to uppercase
    print(f"Octal: {oct(decimal_value)[2:]}")  # Convert to octal, strip '0o' prefix

# Main function to control the flow of the program
def main():
    # Display the menu for selecting the input type
    print("Choose the input type:")
    print("1: Binary")
    print("2: Decimal")
    print("3: Hexadecimal")
    print("4: Octal")

    # Prompt the user to choose an input type
    choice = input("Enter your choice (1/2/3/4): ")

    # Depending on the user's choice, get a valid input for that number system and convert it
    if choice == '1':
        number = get_valid_input('binary')  # Get valid binary number
        convert_number(number, 'binary')  # Convert and display
    elif choice == '2':
        number = get_valid_input('decimal')  # Get valid decimal number
        convert_number(number, 'decimal')  # Convert and display
    elif choice == '3':
        number = get_valid_input('hexadecimal')  # Get valid hexadecimal number
        convert_number(number, 'hexadecimal')  # Convert and display
    elif choice == '4':
        number = get_valid_input('octal')  # Get valid octal number
        convert_number(number, 'octal')  # Convert and display
    else:
        print("Invalid choice")  # Handle invalid input type choice

# Entry point of the program
if __name__ == "__main__":
    main()
