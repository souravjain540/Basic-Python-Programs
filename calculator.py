print("Welcome to basic python calculator", "\n")

while True:
    while True:
        try:
            num1 = int(input("Enter first digit: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    while True:
        try:
            num2 = int(input("Enter second digit: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # Define operations
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2

    # Display operation choices
    print("\nChoose an operation: ")
    print("Press 1 for addition (+)")
    print("Press 2 for subtraction (-)")
    print("Press 3 for multiplication (*)")
    print("Press 4 for division (/)")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == 4:
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Invalid input! Please choose between (1-4)")
                continue  # Ask again if the input is not 1-4
            break  # Exit choice loop after a valid selection
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")

    # Ask if the user wants to continue
    next_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
    if next_calculation == "no":
        print("Goodbye!")
        break
