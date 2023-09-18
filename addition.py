num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sum = num1 + num2

print("Sum of", num1, "and", num2, "is", sum)
# or
print(f"Sum of {num1} and {num2} is {num1+num2}") # didn't use sum variable

# Alternate method
print(f'Sum is {int(input("Enter number 1: ")) + int(input("Enter number 2: "))}')