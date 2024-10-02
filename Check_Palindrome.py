# Palindrome check
def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string = "madam"
print(f"{string} is a palindrome: {is_palindrome(string)}")
