factorials = [1] * 10
for i in range(2, 10):
    factorials[i] = factorials[i-1] * i
sum1 = 0
num = int(input("Enter a number:"))
temp = num
while num:
    r = num % 10  
    sum1 += factorials[r]  
    num //= 10  
if sum1 == temp:
    print("The number is a strong number")
else:
    print("The number is not a strong number")