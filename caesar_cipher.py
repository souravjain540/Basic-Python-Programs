def encrypt(plain_text, shift_amount):
  ciphered_text = ""

  for letter in range(len(plain_text)):
    character = plain_text[letter]

    if (character.isupper()):
      ciphered_text += chr((ord(character) + shift_amount-65) % 26 + 65)

    else:
      ciphered_text += chr((ord(character) + shift_amount - 97) % 26 + 97)

  return ciphered_text

plain_text = input("Enter the text to be ciphered : ")
key = int(input("\nEnter the key/shift amount : "))
print ("\nCiphered text: " + encrypt(plain_text, key))
