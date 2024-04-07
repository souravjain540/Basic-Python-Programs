def CheckLeap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,"is a Leap Year")
    else:
        print(year,"is not a Leap Year")

year = int(input("Enter the year: "))
CheckLeap(year)