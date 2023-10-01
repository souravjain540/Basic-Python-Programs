def encrypt(message, key):
    encrypted_message = ''
    for alphabet in message:
        if alphabet.isalpha():
            encrypted_message += chr(ord(alphabet) - key)
        else:
            encrypted_message += alphabet
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ''
    for alphabet in encrypted_message:
        if alphabet.isalpha():
            decrypted_message += chr(ord(alphabet) + key)
        else:
            decrypted_message += alphabet
    print('Decrypted Message:', decrypted_message)

def main():
    print("Hello Anonymous, you can encrypt or decrypt a message.")
    try:
      choice = int(input('Enter 1 for encryption or 0 for decryption: '))
          
      if choice == 1:
        message = input('Enter any string value: ')
        key = int(input('Enter the shift value: '))
        encrypted_result = encrypt(message, key)
        print('Encrypted Message:', encrypted_result)
      if choice ==0:
        encrypted_message = input('Enter the encrypted message: ')
        key = int(input('Enter the shift value: '))
        decrypt(encrypted_message, key)
      else:
        print('please enter valid  value')
    except  ValueError:
      print('ERROR !!!!!!!!!!!!! please enter only integer 1 and 0')
  

if __name__ == "__main__":
    main()
