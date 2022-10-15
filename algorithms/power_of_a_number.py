def power_of_a_linear(x, n):
    if n == 0:
        return 1
    return x * power_of_a_linear(x, n-1)

x = int(input("Enter the number:"))
n = int(input("Enter the power:"))
print(power_of_a_linear(x, n))
