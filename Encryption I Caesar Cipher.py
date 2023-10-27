text = input("Enter string to encrypt: ")
key = input("Enter key: ")


output = ""
for i in range(len(text)):
    if text[i] == " ":
        output += ' '
    else:
        output += chr((ord(text[i]) - ord("A") - key )%26 + ord("A"))
print(output)