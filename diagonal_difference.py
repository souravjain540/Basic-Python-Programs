# DimitriiTrater


import math
import os
import random
import re
import sys


def absolute_difference(matrix,n):
    """
    Calculate the absolute difference between the sums of its diagonals.

    :param matrix: square matrix
    :return: absolute difference between the sums of its diagonals
    """
    a = []
    b = []
    k = len(matrix[0])-1
    for i in range(n):
        a.append(matrix[i][i])
    for i in range(n):
        b.append(matrix[i][k])
        k -= 1
    j = sum(a)
    m = sum(b)
    n = m - j
    return abs(n)
     

if __name__ == '__main__':

    n = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = absolute_difference(matrix, n)

    fptr.write(str(result) + '\n')

    fptr.close()
