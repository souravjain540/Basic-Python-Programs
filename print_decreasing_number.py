def printDecreasing(n):
    if n == 0:
        return
    print(n)
    printDecreasing(n-1)

n = int(input("Enter the number:"))
printDecreasing(n)
    