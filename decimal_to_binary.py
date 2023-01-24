def dec_to_bin(n:int)->int:
    return int(str(bin(n))[2:])
    
    #bin() is a function that takes in a string and converts it to binary provided the string is purely integer populated



num = int(input('Enter a number (base 10): '))
print("It's value in binary is",dec_to_bin(num))