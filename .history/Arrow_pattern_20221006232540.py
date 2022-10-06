n = int(input())
n1 = (n+1)//2
n2 = n-n1

for i in range(1,n1+1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='')
    print()    

for i in range(n2,0,-1):
    for j in range(1,i):
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='')
    print()        