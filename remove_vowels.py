vowels = ['a', 'e', 'i', 'o', 'u']

text = input("Enter some text: ")

for char in text:
    if(char.lower() in vowels):
        continue
    else:
        print(char, end = '')