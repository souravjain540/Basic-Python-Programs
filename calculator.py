while True:
    # definition for operators
    
    #addition
    def add(num1, num2):
        return num1+num2
    
    #substraction
    def subtract(num1, num2):
        return num1-num2
    
    #multiplication
    def multiply(num1, num2):
        return num1*num2
    
    #division
    def divide(num1, num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            print ("WARNING: Invalid division, cannot divide by zero")
    
    #exponent
    def exponent(num1, num2):
        return num1**num2

    while True:
        try:
            num1=float(input("Enter a digit: "))
            num2=float(input("Enter another digit: "))
            break
        except ValueError:
            print("The input was not a valid digit")

    #command for operation
    print("Choose an operation")
    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for exponent")

    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':      
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "to the power of", num2, "=", exponent(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid input")
