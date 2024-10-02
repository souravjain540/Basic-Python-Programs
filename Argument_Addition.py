# Addition Using *args (Variable Number of Arguments)
def add_multiple_numbers(*args):
    return sum(args)

# Example usage:
print(f"Sum of 1, 2, 3, 4, 5 is {add_multiple_numbers(1, 2, 3, 4, 5)}")
