import datetime

date_one = input("Enter start date (y/m/d): ")
date_two = input("Enter end date (y/m/d): ")
date_one_list = date_one.split("/")
date_two_list = date_two.split("/")
date1 = datetime.date(int(date_one_list[0]),
		      int(date_one_list[1]),
		      int(date_one_list[2]))
date2 = datetime.date(int(date_two_list[0]),
		      int(date_two_list[1]),
		      int(date_two_list[2]))

if date1 > date2:
	difference = (date1 - date2).days
else:
	difference = (date2 - date1).days
print(difference, "days")



