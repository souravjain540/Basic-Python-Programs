def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res = []
    i = 0
        
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
            
    return ''.join(res)


action = input("Do you want to encode or decode, Press 'e' to encode and 'd' to decode: ")

while action != 'e' and action != 'd':
    action = input("Do you want to encode or decode, Press 'e' to encode and 'd' to decode: ")
    print('Your action is', action)

if action == 'e':
    string = input("Enter the string you wish to encode: ")
    print('string is', string)
    print("Encoded string is",encode(string))
elif action == 'd':
    string = input("Enter the string you wish to decode: ")
    print('string is', string)
    print("Decoded string is", decode(string))
