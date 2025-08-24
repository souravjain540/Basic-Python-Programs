try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    num3 = int(input("Enter Third Number: "))
    print("The sum of the three numbers is:", num1 + num2 + num3)
except ValueError:
    print("Invalid input! Please enter valid integers only.")
    exit()
