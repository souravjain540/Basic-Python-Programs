def prime_factors(n):
    final = []
    rstr = ''
    while n != 1:
        for x in range(2,n+1):
            if n % x == 0:
                n //= x
                final.append(x)
                break
    for x in final:
        if f'({x}**{final.count(x)})' in rstr:
            continue
        rstr += f'({x}**{final.count(x)})' if final.count(x) > 1 else f'({x})'
    return rstr

#Function that decomposes number into their base multiplicants. Usefull for simplifications of square roots etc.
#Example: prime_factors(30) outputs (2)(3)(5) because 30 = 2 * 3 * 5
