# Code contributed by @nim09911

import math

def isPrime(num):

    # All numbers < 2 are not Prime
    if(num <= 1):
        return "not Prime"
    
    # if any number from 2 to sqrt(num)
    # does not divide num then num is prime
    for i in range(2, int(math.sqrt(num))+1):
        # check if i divides num using %
        if(num%i==0):
            return "not Prime"
    
    return "Prime"

if __name__ == "__main__":
    
    # Program to check if a number is prime or not
    number = int(input("Enter an Integer: "))
    print(f"{number} is {isPrime(number)}")