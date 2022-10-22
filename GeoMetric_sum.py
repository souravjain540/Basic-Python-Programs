#   Geometric Sum = 1 + 1/2 + 1/4 + 1/8 + 1/16 + ... + 1/(2^n)
#   where n is the input from the user
#   Example:
#   Input: 3
#   Output: 1.875

def geometricSum(n):
    if n == 0:  # base case
        return 1  # return 1 if n == 0
    smallOutput = geometricSum(n - 1)  # recursion call
    # adding and smallOutput vaule + 1 and divide using 2^n
    return smallOutput + 1 / pow(2, n)


n = int(input())  # taking input from user
print(geometricSum(n))  # calling the function and printing the result
