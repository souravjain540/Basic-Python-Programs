# Function to check if the number is palindrome or not

def checkPalindrome(check):
    palin = 0
    rev = check
    while( rev > 0):
        rem = rev % 10
        palin = (palin * 10) + rem
        rev //= 10

    if check == palin :
        print(check, "is a palindrome number :D ")
    else:
        print("Sorry, " , check , " is not a palindrome number :(")

check = int(input("Please an enter to number :"))
checkPalindrome(check)
