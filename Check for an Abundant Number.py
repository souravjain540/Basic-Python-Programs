# A number that is smaller than the sum of all its factors except the number itself is known as an abundant number 

num = int(input("Enter the number : "))
add = 0 
for i in range(1, num):
    if (num%i==0):
        add = add + i
        
if (num<add):
    print(f'{num} is an abundant number')
else:
    print("It is not an abundant number")