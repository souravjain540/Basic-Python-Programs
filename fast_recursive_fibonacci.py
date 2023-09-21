def fast_rec_fib_helper(n):
    """returns the last two elements of the fibonacci sequence."""
    if n <= 1:
        return (0,1)
    m = n//2
    hprv, hcur = fast_rec_fib_helper(m)
    prev = (hprv ** 2) + (hcur **2)
    curr = hcur * (2 * hprv + hcur)
    next = prev + curr
    if n % 2 == 0:
        return (prev, curr)
    else:
        return (curr, next)

def fast_rec_fib(n):
    if n==0:
        return 0
    previous, current = fast_rec_fib_helper(n)
    return current

print(fast_rec_fib(2))