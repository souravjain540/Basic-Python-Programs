 import math

n = int(input())
p = []

def isprime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

for i in range(n):
    if isprime(i):
        p.append(i)

print(p) 
