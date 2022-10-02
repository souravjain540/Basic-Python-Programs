str_1 = input ("Enter the string to check if it is a palindrome: ")
str_1 = str_1.casefold ()
rev_str = reversed (str_1)
if list (str_1) == list (rev_str):
    print ("The string is a palindrome.")
else:
    print ("The string is not a palindrome.")
