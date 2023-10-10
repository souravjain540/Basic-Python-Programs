n = int(input("Enter the number:\t"))
r = 0
while n>0:
    remi = n%10
    r = r*10 + n%10
    n = n//10
print(r)
