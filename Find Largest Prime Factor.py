def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True
inp = int(input("Enter number: "))

if isPrime(inp):
    print("Largest Prime Factor:", inp)
    exit()

for j in range(inp+1, 0, -1):
    if inp%j==0 and isPrime(j):
        print("Largest Prime Factor:", j)
        break