'''
this function will take two numbers, list down their multiples in range of natural numbers and will print their sums

for example: 

the two numbers are 2 and 3 and I choose to low_bound to be 1 and up_bound to be 10 (which means from 1 to 10)

then, this program will the multiples of 2 and 3 between the numbers 1 to 10: 
which is --> 2,3,4,6,8,9 
then it will add all ^^these numbers and print 2+3+4+6+8+9=32

'''

def whichIsSmall(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

def multiplesum(num1, num2, low_bound, up_bound): # the main function which finds the multiples and add them up

    smallest_multiple = whichIsSmall(num1, num2)

    if up_bound % smallest_multiple == 0:
        limit = 1
    else:
        limit = up_bound % smallest_multiple

    sum = 0

    for i in range(low_bound,up_bound):
        if (i % num1 == 0 or i % num2 == 0):
            
            if i == up_bound-limit:
                print(f"{i}", end="=")
                sum += i
            else:

                print(f"{i}", end="+")
                sum += i

    print(f"{sum}")

if __name__ == "__main__":
    
    num1 = int(input("Enter your first number: "))   
    num2 = int(input("Enter your second number: "))
    low_bound = int(input("Enter the lower limit: "))
    up_bound = int(input("Enter the upper limit: "))

    multiplesum(num1, num2, low_bound, up_bound)
