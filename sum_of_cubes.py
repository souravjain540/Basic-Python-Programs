# This is the program to get the sum of cubes of first n natural numbers;

def sumofcubes(n):
    counter = 0
    for i in range(1, n+1):
        counter = counter+(i*i*i)
    return counter

print(sumofcubes(3))
