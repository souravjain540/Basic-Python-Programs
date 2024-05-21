import math

def baseDigits():
       n = eval(input("Enter a number in base 10: "))
       base = eval(input("What base do you want? "))
       numDigits = int(math.log(n, base)) + 1
       print("That number has", numDigits, "digits in base", base)
       newNum = ""
       placeValue = 1
       for _ in range(numDigits):
           digit = n % base
           newNum = str(digit) + newNum
           print(digit, "is in the", placeValue, "'s place")
           n = n // base
           placeValue = placeValue * base
       return n, base, newNum
       
n, base, newNum = baseDigits()
print("{:d} in base {:d} is {:s}".format(n, base, newNum))
       
