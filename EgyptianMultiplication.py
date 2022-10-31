def multiply(n1,n2):
  tot = 0
  while n2 > 0:
    if n2 % 2 == 1:
      tot += n1
    n1 *= 2
    n2 //= 2
    print (n1, n2)
  return tot
