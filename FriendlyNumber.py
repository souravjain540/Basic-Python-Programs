def proper_divisors_sum(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum


def are_friendly_numbers(num1, num2):
    sum1 = proper_divisors_sum(num1)
    sum2 = proper_divisors_sum(num2)
    return sum1 == num2 and sum2 == num1


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if are_friendly_numbers(num1, num2):
        print(f"{num1} and {num2} are friendly numbers.")
    else:
        print(f"{num1} and {num2} are not friendly numbers.")

except ValueError:
    print("Please enter valid integers.")
