"""
    Program to get maximum length substring from a given string.

    For example:
    STRING : 'malayalam'
    OUTPUT : 'malayalam'

    STRING : 'aabaaaacaaaa'
    OUTPUT : 'aaaacaaaa'

    STRING : 'abc'
    OUTPUT : 'a'
"""

def maximum_substring_palindrome(string: str) -> str:
    n = len(string)
    palindrom_matrix = [[0] * n for _ in range(n)]
    substr_idx = [0, 0]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                palindrom_matrix[i][j] = 1
            elif j - i == 1:
                palindrom_matrix[i][j] = (int) (string[i] == string[j])
            elif (i + 1 < n and j - 1 > -1 and palindrom_matrix[i + 1][j - 1] == 1 and string[i] == string[j]):
                palindrom_matrix[i][j] = 1
            
            if palindrom_matrix[i][j] == 1:
                if j - i >= substr_idx[1] - substr_idx[0]:
                    substr_idx = [i, j]

    return string[substr_idx[0]: substr_idx[1] + 1]

if __name__ == "__main__":
    STRING: str = "aabaaaacaaaa"
    MAX_PALINDROME = maximum_substring_palindrome(STRING)

    print("Maximum substring palindrom : ", MAX_PALINDROME)