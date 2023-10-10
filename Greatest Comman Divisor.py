a = int(input("Enter the 1st number:\t"))
b = int(input("Enter the 1st number:\t"))
l1 = []
l2 = []
l = []
for i in range(1,a+1):
    if a%i==0:
        l1.append(i)
for j in range(1,b+1):
    if b%j==0:
        l2.append(j)
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            l.append(l1[i])
l.sort()
print(l[-1])