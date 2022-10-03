def gcd(a, b):
    if b == 0:
        return a
    elif a < b :
        return gcd(b, a)
    return gcd(b, a%b)
    
    
if __name__ == "__main__" :
    a, b = map(int, input().split())
    print("GCD of", a,"and", b, "is", gcd(a, b))
