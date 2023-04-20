# Calculate the complete age of a person in years, months and days

import datetime

# Function which calculates age of a person
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                                    #The above code return 1 if the above statement is true

def main():

    # Get the date of birth and stores it in dob
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    # Split the date into year, month and day
    year, month, day = map(int, dob.split('-'))

    # Calculate the age by inputing it to the function calculate_age()
    age = calculate_age(datetime.date(year, month, day))

    # Print the age
    print("Your age is: {}".format(age))

if __name__ == '__main__':
    main()
