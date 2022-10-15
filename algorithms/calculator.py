num1=int(input("eneter a digit"))
num2=int(input("eneter a another digit"))
# defination for operators

#addition
def add(num1, num2):
    return num1+num2
#substraction
def subtract(num1, num2):
    return num1-num2
#multiply
def multiply(num1, num2):
    return num1*num2
#division
def divide(num1, num2):
    return num1/num2

#command for operation
print("choose operation")
print("press 1 for add")
print("press 2 for subs")
print("press 3 for multiply")
print("press 4 for devision")





while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))



        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':      
            print(num1, "*", num2, "=", multiply(num1, num2))





        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
