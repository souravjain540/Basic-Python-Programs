"""
    This is Leetcode question: https://leetcode.com/problems/reverse-words-in-a-string/
    
"""

def reverseWords(s: str) -> str:
    s = s.split()
    s.reverse()
    return " ".join(s)


assert reverseWords("     Hello World   ")=="World Hello"
assert reverseWords("a good   example")=="example good a"
assert reverseWords("okay")=="okay"
