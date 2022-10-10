"""
Python program to find sum of divisors of a number n,
for example:
print(sum_divisors(0))
# 0
print(sum_divisors(3)) 
# Should sum of 1
# 1
print(sum_divisors(36)) 
# Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) 
# Should be sum of 2+3+6+17+34+51
# 114
 """


def sum_divisors(n):
    sum = 0
    x = 1
    while x < n:
        if n % x == 0:
            sum += x
        else:
            x += 1
            
    return sum



