print("Ticket price for adults is : Rs. 40\nTicker price for children is : Rs. 20")
adult_tkts = int(input("Enter the number of adults : "))
child_tkts = int(input("Enter the number of adults : "))
total = adult_tkts*40 + child_tkts*20
if total>=1000:
    dis=0.05*total
elif total>=500 and total<1000:
    dis=0.02*total
else:
    dis=0
final=total-dis
print("Total Price is : ", total)
print("You got a group discount of : ", dis)
print("After discount pay : ", final)
