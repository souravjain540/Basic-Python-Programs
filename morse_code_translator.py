# Morse Code Translator in Python

# Dictionary mapping letters and numbers to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Function to translate text to Morse code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '  '  # Separate words with double space
    return morse_code

# Function to translate Morse code to text
def morse_to_text(morse_code):
    text = ''
    morse_code += ' '  # Ensure the last code is processed
    morse_char = ''
    space_count = 0
    for char in morse_code:
        if char != ' ':
            space_count = 0
            morse_char += char
        else:
            space_count += 1
            if space_count == 1:  # End of a character
                if morse_char in MORSE_CODE_DICT.values():
                    text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
                morse_char = ''
            elif space_count == 3:  # End of a word
                text += ' '
    return text

# Main program
if __name__ == "__main__":
    while True:
        print("\nMorse Code Translator")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        choice = input("Choose an option (1/2): ")
        if choice == '1':
            text = input("Enter text to translate: ")
            print("Morse Code:", text_to_morse(text))
        elif choice == '2':
            morse_code = input("Enter Morse code to translate: ")
            print("Text:", morse_to_text(morse_code))
        else:
            print("Invalid choice. Please enter 1 or 2.")

        if input("\nTranslate another? (y/n): ").lower() != 'y':
            break
