import string

n = int(input())
s = input().lower()
if set(string.ascii_lowercase).issubset(s):
    print("YES")
else:
    print("NO")
