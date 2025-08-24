 # In this program we will convert numbers to words
 # For example: 123 -> One Two Three
def number_to_words(number):
# Define a mapping of digits to words
    digit_to_word = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    result=[]
    # Convert the number to string to iterate over each digit
    for digit in str(number):
        if digit in digit_to_word:
            result.append(digit_to_word[digit])
        else:
            return "Invalid input! Please enter a valid non-negative integer."
    return ' '.join(result)
# Example usage
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print("Number in words:", number_to_words(number))