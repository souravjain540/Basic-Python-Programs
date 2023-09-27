# Check The Prime Factors 

n = int(input("Enter the number : "))
arr = []
for i in range(2, n):
    if n % i == 0:
        arr.append(i)
print(arr)
sol = []

for j in arr:
    flag = 0
    for k in range(2, j):
        if j % k == 0:
            flag = 1 
            break 
    if flag == 0:
        sol.append(j)
        

print("The Prime Factors of the number are: ")
for m in sol:
    print(m, end=' ')
        