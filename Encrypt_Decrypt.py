def main():

    choice  = input("Type 'encode' to encrypt, Type 'decode' to decrypt\n").lower()
    text = input("Type your message (only text message without spaces): \n").lower()
    shift = int(input("Type your shift number: \n"))
    if choice == "encode":
        text_encrypt1 (text,shift)
    elif choice == "decrypt":
        text_decrypt1 (text,shift)
    else :
        print("You should have entered correct choice!!")
    return 0

alphabet = ["a","b","c","d","e","f","g","h","k","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def text_encrypt1 (string,shift):
    for i in range(len(list(string))):
        if string[i] in alphabet:
            length=alphabet.index(string[i])+shift 
            if length>25:
                length-=26
                print(alphabet[length],end="")
            else :
                print(alphabet[length],end="")
    return 0

def text_decrypt1 (string,shift):
    for i in range(len(list(string))):
        if string[i] in alphabet:
            length=alphabet.index(string[i])-shift 
            if length<0:
                length+=26
                print(alphabet[length],end="")
            else :
                print(alphabet[length],end="")
    return 0

# Functions mentioned below provide another way to do the same but below here due to shift parameter not being restricted
# to be within range of all alphabets it can display other special characters as ascii values are used here
# According to methese functions are more general as it accounts for all types of characters in message. 
# Some changes are to be made in the future, will make this program more better.

def text_encrypt2 (string,shift):
    for i in list(string):
        if i in list(string):
            print(chr(ord(i)+shift),end="")
    return 0

def text_decrypt2 (string,shift):
    for i in list(string):
        if i in list(string):
            print(chr(ord(i)-shift),end="")
    return 0
       
if __name__ == "__main__":
    main()
