a=int(input("enter a number:"))
sum=0
while(a!=0):
    b=a%10
    sum=sum+int(b)
    a=a/10
print(int(sum))    