def is_palindrome(x):
    return str(x) == str(x)[::-1]

# Example Usage:
x = 121
print(is_palindrome(x))  # Output: True
