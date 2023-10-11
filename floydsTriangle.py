# Floyd's triangle

m = 5
num = 0
# outer loop
for i in range(1, 6):
    # inner loop
    for i in range(1, i+1):
        num += 1
        print(num , end=" ")
    print()