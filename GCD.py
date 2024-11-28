def gcd(p,q):
    gcd =1
    if p%q==0:
        return q
    for z in range(int(q/2), 0,-1):
        if (p%z==0) and (q%z==0):
            gcd = z
            break

print(gcd(4,3))        