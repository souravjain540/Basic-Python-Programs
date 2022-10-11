def is_narcissist(number):
    l = len(str(number))
    tmp = number
    sum = 0
    while(tmp > 0):
        sum += (tmp % 10) ** l
        tmp = int(tmp / 10)
    return number == sum
    
n = int(input("Enter a number: "))
narc = "is" if is_narcissist(n) else "is not"
print(f'{n} {narc} a narcissistic number')