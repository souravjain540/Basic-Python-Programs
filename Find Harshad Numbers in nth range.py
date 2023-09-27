# Print Harshad Number in nth range 

range = int(input("Enter the range : "))

for i in range(1, range):
    add = 0 # Always Better To Use Flag Equations in Outer Loop 
    for j in str(i):
        add = add + int(j)
    if (i %add == 0):
        print(i)
        