import time
import math
s="=====MENU====="
t="exiting...."
p=["1. Area of Circle","2. Area of Square","3. Area of Rectangle","4. Area of Triangle","5. Exit"]
for i in s:
    print(i,end="")
    time.sleep(0.1)
print()
for i in p:
    for j in i:
        print(j,end="")
        time.sleep(0.1)
    print()
while True:
    try:
        c=int(input("Enter your choice: "))
        if c==1:
            r=float(input("Enter radius: "))
            print("Area of circle is: ",math.pi*r*r)
        elif c==2:
            l=float(input("Enter length: "))
            print("Area of square is: ",l*l)
        elif c==3:
            l=float(input("Enter length: "))
            b=float(input("Enter breadth: "))
            print("Area of rectangle is: ",l*b)
        elif c==4:
            b=float(input("Enter base: "))
            h=float(input("Enter height: "))
            print("Area of triangle is: ",0.5*b*h)
        elif c==5:
            for i in t:
                print(i,end="")
                time.sleep(0.1)
            break
        else:
            print("Invalid choice")

    except:
        print("Invalid input")
    print()
