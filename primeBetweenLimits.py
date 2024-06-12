a=int(input("Enter the lower limit number: "))
b=int(input("Enter the upper limit number: "))
if(a>b):
    t=a
    a=b
    b=t
w=[]
d=0
for c in range(a,b+1):
    for k in range(2,c):
        if(c%k==0):
            break
    else:
        d+=1
        w.append(c)
if(d==0):
    print("No prime number exists between the given limits.")
else:
    print(f"There exists {d} prime number(s). They are",end='')
for y in w:
    print(", ",y,end='')
print(".")
