# Find the largest of three numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage:
a, b, c = 10, 20, 15
print(f"The largest of {a}, {b}, and {c} is {find_largest(a, b, c)}")
