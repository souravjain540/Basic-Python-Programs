def bin_to_dec(n:int)->int:
    return int(str(n),2)
    


num = int(input('Enter a number (base 2): '))
print("It's value in base 10 is",bin_to_dec(num))