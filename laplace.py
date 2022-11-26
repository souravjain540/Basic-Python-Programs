import numpy as np
import copy

matrix_A = [[2,4,22,34],[53,6,5,142],[2,3,34,42], [42, 23, 2, 8]]
# matrix_A = [[1, 2, 3], [1, 4, 3], [1, 5, 3]]

def matrix_size(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    if rows == columns:
        return rows, columns
    else:
        print("matrix aint valid chief")

def delete(matrix, x, y):
    minor = copy.deepcopy(matrix)
    minor = np.delete(minor, y, 1)
    minor = np.delete(minor, x, 0)
    return minor

def laplace_det(matrix, columns):
    rows, columns = matrix_size(matrix)

    if columns == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(columns):
        det += matrix[i][0] * (-1) ** (i + 2) * laplace_det(delete(matrix, i, 0), columns - 1)
    return det


print(laplace_det(matrix_A, 3))


