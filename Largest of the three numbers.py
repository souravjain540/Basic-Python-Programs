# Largest number from the given three numbers


# Take the input from the user 
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

a = float(input("Enter the first number - "))
b = float(input("Enter the second number - "))
c = float(input("Enter the third number - "))
print(maximum(a, b, c))