import time
start_time = time.time()

# def permutation(elements):
#     results = []
#     if len(elements) <= 1:
#         results.append(elements)
#         return results
#     for perm in permutation(elements[1:]):
#         for i in range(len(elements)):
#             results.append(perm[:i] + elements[0:1] + perm[i:])
#     return results

# print(permutation([1,2,3,4]))

def all_possible(*args, perm_lenght=4):
    pools = [pool for pool in args] * perm_lenght
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for product in result:
        yield product

# for i in all_possible(range(4)):
#     print(i)

def permutations(iterable):
    pool = iterable
    n = len(pool)
    for indices in all_possible(range(n), perm_lenght=n):
        if len(set(indices)) == n:
            yield [pool[i] for i in indices]

def parity(p, x):
    par =  sum(1 for (x, px) in enumerate(p)
                 for (y, py) in enumerate(p)
                 if x < y and px > py) % 2 == 0
    if par: return x
    else: return -x

def determinant(matrix):
    n = len(matrix)

    det = 0
    for sigma in permutations(range(n)):
        prod = 1
        for i in range(n):
            prod *= matrix[i][sigma[i]]
        det += parity(sigma, prod)
    return det
    # return sum(parity(z, math.prod([matrix[i][sigma[i]] for i in range(n)])) for sigma, z in zip(permutations(range(n)), p))

print(determinant([[2,4,22,34],[53,6,5,142],[2,3,34,42], [42, 23, 2, 8]]))

print("--- %s seconds ---" % (time.time() - start_time))
