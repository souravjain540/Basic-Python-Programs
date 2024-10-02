# Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")
