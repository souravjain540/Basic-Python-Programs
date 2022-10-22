import calendar
'''
Write a Python program that prints the calendar of a given month in a given year after validating the user input.
'''


def validate_user_input():
    is_valid_year = False
    is_valid_month = False
    '''user should enter a valid year'''
    while not is_valid_year:
        year = input("Enter the year \n format: YYYY:  ")
        if len(year) == 4 and year.isdigit():
            is_valid_year = True
        else:
            print("Kindly Enter a vaild four-digit year number")
        '''user should enter a valid month'''
    while not is_valid_month:
        month = input("Enter month \n format: 1-12:  ")
        if month.isdigit() and 12 >= int(month) >= 1:
            is_valid_month = True
        else:
            print("Kindly Enter a vaild month number between 1 and 12")
    return [int(year), int(month)]


def print_given_month():
    year, month = validate_user_input()
    print(year, month)
    print(calendar.month(year, month))


print_given_month()