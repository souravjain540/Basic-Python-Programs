"""
#ATM Machine Using python
This is a simple python program which aims to mimic the functions of an atm.
It contains check BALANCE, withdraw, payin and retrive card features.

Original Author: Unknown

Contributors: (Add your name if you are a part)
Ruhan Saad Dave [https://github.com/Ruhan-Saad-Dave]
#And other contributors which I have no knowledge of.

Last update: (Change this everytime you update it)
Fixed the negative BALANCE glitch, made the program more optimised, and added comments for explaination.
"""

print("="*30, "Welcome to Python Bank ATM", "="*30)    #Initial welcome statement

#Global variables
CHANCES= 3 
BALANCE = 1000
PIN = '1234'

while CHANCES > 0:
    '''
    This checks if the user has entered correct password or not.
    If more than 3 times incorrect then calls the police.
    '''
    pin = input("Please enter your 4 Digit pin: (Default = 1234)")
    if pin == PIN:
        print("\nCorrect pin!!\nLoading bank details...\n")
        break
    else:
        print("\nINCORRECT PIN!!\n")
        CHANCES -= 1
else:
    print("\nYou ran out of CHANCES\nCalling the Police...\n")

while CHANCES >0:
    '''
    This is the main program, will work if the user didnt run out of chance. 
    Used separate loop instead of nested loop to bring optimisation.
    '''
    print("\n\n\n1 ~ Your Balance")
    print("2 ~ Make a Withdrawal")
    print("3 ~ Pay In")
    print("4 ~ Return Card")
    option = input("Enter your option: ")
    print('\n' * 2)

    if option == '1':    #Checks for balance
        print(f"Your Balance is: ${BALANCE}")

    elif option == '2':    #Withdraw money if after withdraw have non-negative balance.
        withdrawl = float(input("How Much Would you like to withdraw?: "))
        if BALANCE - withdrawl < 0:
            print("Insufficient BALANCE!")
            next = input("Press enter to continue.")
        else:
            BALANCE -= withdrawl
            print(f"Your BALANCE after the withdrawl is ${BALANCE}")
            next = input("Press enter to continue.")
                
    elif option == '3':    #Put in money into the bank
        pay_in = float(input("How Much Would you like to Pay In? "))
        BALANCE = BALANCE + pay_in
        print(f"Your BALANCE after the Pay-in is ${BALANCE}")
        next = input("Press enter to continue.")

    elif option == '4':    #Taking the card out and exiting the program.
        print("Please wait whilst your card is Returned....\nThank you for your patience.")
        break

    else:
        print("Invalid option, please try again.")

#End of program.