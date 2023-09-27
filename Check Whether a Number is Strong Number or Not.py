# Check Whether a Number is Strong Number or Not

n = int(input("Enter a number : "))

digits = []
for i in str(n):
    digits.append(int(i))
add = 0  
for i in digits:
    product = 1
    for j in range(1, i+1):
        product = product * j
    add = add + product
print(add)
if (n==add):
    print("It is a strong number")
else:
    print("It is not a strong number")