def swap(p, q):
    temp_1 = p
    p = q
    q = temp_1
    print ("The Value of P after swapping: ", p) 
    print ("The Value of Q after swapping: ", q)
# Usage 
p = int(input("Enter p: "))
q = int(input("Enter q: "))
swap(p, q)
