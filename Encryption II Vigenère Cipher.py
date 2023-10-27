text = input("Enter string to encrypt: ")
key = input("Enter key: ")

# text = "DASHBOARD"
# key = "LINUX"
key = key*(len(text)//len(key) + 1)
key = key[:len(text)]

output = ""
for i in range(len(text)):
    
    output += chr((ord(text[i]) - ord("A") + ord(key[i]) - ord("A"))%26 + ord("A"))
print(output)