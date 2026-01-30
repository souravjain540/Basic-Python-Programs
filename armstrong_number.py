number = int(input("Enter a number: "))
sum_of_powers = 0
temp = number
digits = len(str(number))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

if number == sum_of_powers:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
