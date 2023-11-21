def det(M):
    d = 0
    if len(M)==2:
        return M[0][0]*M[1][1]-M[1][0]*M[0][1]
    else:
        n = len(M)
        for i in range(n):
            a = [row[:i] + row[i + 1:] for row in M[1:]]
            d += M[0][i] * det(a) * (-1)**i
    return d
L1 = [[1, 2, 3], [-1, 2, 4], [0, 1, 3]] #this can be taken as input as well 
print("determinant = ",det(L1))
