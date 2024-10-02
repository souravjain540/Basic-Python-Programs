def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example Usage:
n = 5
print(climb_stairs(n))  # Output: 8
