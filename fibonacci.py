def fibonacci_of(n):
  if n in {0, 1}:
    return n
  return fibonacci_of(n - 1) + fibonacci_of(n - 2)
for i in range(1,100):
  print(fibonacci_of(i))
