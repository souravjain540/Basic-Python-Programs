def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
def lcm(a,b):
    return (a / gcd(a,b))* b
 
print('GCD of', 15, 'and', 20, 'is', gcd(15,20))
print('LCM of', 15, 'and', 20, 'is', lcm(15, 20))