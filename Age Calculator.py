# Calculate the complete age of a person in years, months and days

import datetime

def calculate_age(born):
    today = datetime.date.today()
    months = 0
    days = 0
    if today.month < born.month or (today.month == born.month and today.day < born.day):
        months += today.month - 1
        days += today.day
    elif today.month == born.month and today.day > born.day:
        days += (today.day - born.day)
    else:
        months += (today.month - born.month)
        days += today.day
    print(today.day)
    return [today.year - born.year - ((today.month, today.day) < (born.month, born.day)), months + (12-born.month), days]

def main():

    # Get the date of birth
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Split the date into year, month and day
    year, month, day = map(int, dob.split('-'))

    # Calculate the age
    age = calculate_age(datetime.date(year, month, day))

    # Print the age
    print(f"Your age is: {age[0]} years, {age[1]} months and {age[2]} days")#.format(age))

if __name__ == '__main__':
    main()