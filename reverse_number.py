"""This file has the function which reverses real integer."""


def reverse_number(number: int) -> int:
    """
    This function reverses a number where number can be real integer
    """
    if number == 0:
        return 0

    sign = 1 if number > 0 else -1
    number = abs(number)
    reverse = 0
    while number > 0:
        current_digit = number % 10
        reverse = reverse * 10 + current_digit
        number //= 10
    return reverse if sign == 1 else reverse * -1   

N = 567
print(reverse_number(N))


N = 0
print(reverse_number(N))


N = -35670
print(reverse_number(N))
