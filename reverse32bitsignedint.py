# reverse a 32 bit signed int
# if ans overflows then returns 0
def reverse32bitsignedint(n):
    is_negative = 0
    if n < 0:
        is_negative = 1
        n = -n
    ans = 0
    while n:
        quotient = n // 10
        remainder = n % 10
        n = quotient
        ans = ans * 10 + remainder
    limit = 1 << 31
    if is_negative:
        ans = -ans
    if (ans <= -limit) or (ans >= limit - 1):
        return 0
    return ans
