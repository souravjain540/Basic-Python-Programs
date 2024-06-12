def isPalindrome(num):
    number = num
    result = 0
    while number: #while number does not equal to 0
        result = result * 10 + number % 10
        number //=10

    return result == num


def isPalindrome(x):
    #easier implementation
    return str(x) == str(x)[::-1]
