####################################################################################################

# Question
# Write a Python script that reads any integer and asks the user to choose which option to convert:
# 1 for Binary
# 2 for Octal
# 3 for Hexadecimal

####################################################################################################
num = 0
num = int(input("\nDigit an integer positive or -1 to finish: "))

while num != -1:
    print("""
    Choose one of the bases to convert:

    [ 1 ] convert to BINARY
    [ 2 ] convert to OCTAL
    [ 3 ] convert to HEXADECIMAL
    """)

    option = int(input("Your choose: "))

    if option == 1:
        print(f"\n{num} converted to BINARY is {bin(num)[2:]}")
    elif option == 2:
        print(f"\n{num} converted to OCTAL is {oct(num)[2:]}")
    elif option == 3:
        print(f"\n{num} converted to HEXADECIMAL is {hex(num)[2:].upper()}")
    else:
        print("\n #### Invalid option. Try again. ####")

    num = int(input("\nDigit an integer positive or -1 to finish: "))
    
print("Bye!!!")
####################################################################################################
