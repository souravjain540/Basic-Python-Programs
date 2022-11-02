def is_prime(x):
    if x<=3:
        return x>1
    if not x%2 or not x%3:
        return False
    i=5
    max=int(x**0.5)
    while i <= max:
        if not x%i or not x%(i+2):
            return False
        i+=6
    return True

number = int(input("Enter number to check: "))

if is_prime(number):
    print(str(number)+" is a prime")
else:
    print(str(number)+" is not a prime")