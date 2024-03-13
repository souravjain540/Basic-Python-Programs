def caesar_cipher(text, shift, encrypt=True):
    """
    Encrypts or decrypts the input text using the Caesar cipher.
    
    Parameters:
    - text: The input text to encrypt or decrypt.
    - shift: The number of positions to shift each character (the key).
    - encrypt: Specifies the operation; True for encryption, False for decryption.
    
    Returns:
    - The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            start = 'A' if char.isupper() else 'a'
            # Shift the character
            result += chr((ord(char) + (shift if encrypt else -shift) - ord(start)) % 26 + ord(start))
        else:
            # Non-alphabetical characters remain the same
            result += char
    return result

def process_file(filename, shift, encrypt=True):
    """
    Encrypts or decrypts the contents of a file.
    
    Parameters:
    - filename: The name of the file to process.
    - shift: The number of positions to shift each character.
    - encrypt: Specifies the operation; True for encryption, False for decryption.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Encrypt or decrypt the content
        processed_content = caesar_cipher(content, shift, encrypt)
        
        # Save the processed content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        
        print("Operation completed successfully.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    choice = input("Do you want to encrypt or decrypt a file? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return
    
    filename = input("Enter the filename: ")
    shift = int(input("Enter the shift key (number): "))
    process_file(filename, shift, encrypt=(choice == 'e'))

if __name__ == "__main__":
    main()
