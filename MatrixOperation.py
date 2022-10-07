#Prgram Code Created by Shivsagar Mishra
#This is a program to perform basic matrix operarations such as 1. Addition 2.Substraction 3.Multiplication 4.Transpose


import numpy as np

# Initialize matrix
a = np.array([[1,2,1], [6,5,4], [9,5,8]])
b = np.array([[3,2,1], [8,6,4], [4,0,0]])

while True:
    print("List of operations:\n1.Display\n2.Addition\n3.Substraction\n4.Multiplication\n5.Transpose")
    counter=int(input("Enter the your Choice:"))

    if counter == 1:
        #printing 1st matrix
        print("First Matrix:")
        print (a,"\n")
        # printing 2nd Matrix
        print("Second Matrix:")
        print(b,"\n")

    elif counter == 2:
        print ("The addition of matrices is : ")
        print(a.__add__(b),"\n")

    elif counter == 3:
        print ("The Substraction of matrices is : ")
        print ("Substraction is:")
        print(a.__sub__(b),"\n")

    elif counter == 4:
        print ("The multiplication of matrices is : ")
        print(a.__mul__(b),"\n")

    elif counter == 5:
        print ("The Transposition of First matrix is: ")
        print(np.transpose(a),"\n")
        print("The Transposition of Second Matrix is:")
        print(np.transpose(b),"\n")
    else:
        print("Invalid Option!")

    cont=int(input("Do you want to continue?: 1.Yes\t 2.No\t Enter your choice:"))
    if cont==1:
        continue
    else:
        break

