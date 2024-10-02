def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x != 0:
        rev = rev * 10 + x % 10
        x //= 10
    rev = sign * rev
    return rev if -2**31 <= rev <= 2**31 - 1 else 0

# Example Usage:
x = 123
print(reverse(x))  # Output: 321
