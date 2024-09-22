def Fibonacci(num):
    a, b = 0, 1
    if num == 0:
        return "Enter Valid Number"
    elif num == 1:
        return b
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return c

num = int(input("Enter the Number of Fibonacci Series : "))
print(Fibonacci(num))