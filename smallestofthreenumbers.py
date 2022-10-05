# Smallest of the given three numbers
# Taking the input from the user 
num1 = float(input("Enter the first number - "))
num2 = float(input("Enter the second number - "))
num3 = float(input("Enter the third number - "))

if(num1 <= num2) and (num1 <= num3):
   smallest = num1
elif(num2 <= num3) and (num2 <= num1):
   smallest = num2
else: 
   smallest = num3

print("The smallest number is", smallest)   