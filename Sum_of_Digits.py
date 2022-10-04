# Program for sum of digits

def sumOfDigits(n):
    if n == 0:  # base case
        return 0  # if n== 0 than return 0
    # return last digit + sum of digit of remaining number
    return (n % 10 + sumOfDigits(int(n/10)))


n = int(input("Enter the number: "))  # taking input from user
sumOfDigits(n)  # calling the function
