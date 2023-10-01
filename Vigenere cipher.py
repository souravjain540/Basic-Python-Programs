"""
    The Vigenère cipher is a type of encryption that uses a keyword to shift letters in a message by varying amounts, 
    making it more secure than simpler methods like the Caesar cipher. 
    The same keyword is needed to decrypt the message.
"""

def vigenere_encode(plain_text, key):
    # Initialize variables
    encrypted_text = ""
    key_length = len(key)

    # Loop through each character in the plain_text
    for i in range(len(plain_text)):
        # Get the current character from the plain_text
        char = plain_text[i]

        # Check if the character is alphabetic
        if char.isalpha():
            # Determine the shift value based on the corresponding character in the key
            shift = ord(key[i % key_length].lower()) - ord('a')

            # Check if the character is uppercase or lowercase and apply the shift accordingly
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            # If the character is not alphabetic, leave it unchanged
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

def vigenere_decode(encrypted_text, key):
    # Initialize variables
    plain_text = ""
    key_length = len(key)

    # Loop through each character in the encrypted_text
    for i in range(len(encrypted_text)):
        # Get the current character from the encrypted_text
        char = encrypted_text[i]

        # Check if the character is alphabetic
        if char.isalpha():
            # Determine the shift value based on the corresponding character in the key
            shift = ord(key[i % key_length].lower()) - ord('a')

            # Check if the character is uppercase or lowercase and apply the shift accordingly
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        else:
            # If the character is not alphabetic, leave it unchanged
            decrypted_char = char

        plain_text += decrypted_char

    return plain_text

if __name__ == "__main__":
    while True:
        choice = input("Enter 1 to encrypt, 2 to decrypt, or 0 to exit: ")
        if choice == "1":
            plain_text = input("Enter words to be encrypted: ")
            key = input("Enter encryption key: ")
            print(f"Encrypted message: {vigenere_encode(plain_text, key)}")
        elif choice == "2":
            encrypted_text = input("Enter words to be decrypted: ")
            key = input("Enter decryption key: ")
            print(f"Decrypted message: {vigenere_decode(encrypted_text, key)}")
        elif choice == "0":
            break
