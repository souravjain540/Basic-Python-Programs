#Check a number if it's odd or even.

number = int(input("Which number do you want to check? "))


calc = number % 2

if calc == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
