# Code contributed by @nim09911

def gcd(a, b):

    if(a == 0):
        return b
    else:
        return gcd(b%a, a)

if __name__ == "__main__":
    
    # Program to find GCD or HCF
    # of two integers using Euclids Algorithm

    # input
    number1 = int(input("Enter Integer 1: "))
    number2 = int(input("Enter Integer 2: "))
    
    # gcd(smaller number, larger number)
    if(number1 >= number2):
        number1, number2 = number2, number1

    # output
    print(f"GCD({number1}, {number2}) is {gcd(number1, number2)}")