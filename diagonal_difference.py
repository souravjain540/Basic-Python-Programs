# DimitriiTrater

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    a = []
    b = []
    #print(arr)
    k = len(arr[0])-1
    for i in range(n):
        a.append(arr[i][i])
    for i in range(n):
        b.append(arr[i][k])
        k -= 1
    #print(a, b)
    j = sum(a)
    #print(j)
    m = sum(b)
    #print(m)
    n = m - j
    #print(n)
    return abs(n)
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
