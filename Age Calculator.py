# Calculate the complete age of a person in years, months and days

import datetime

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def main():

    # Get the date of birth
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Split the date into year, month and day
    year, month, day = map(int, dob.split('-'))

    # Calculate the age
    age = calculate_age(datetime.date(year, month, day))

    # Print the age
    print("Your age is: {}".format(age))

if __name__ == '__main__':
    main()