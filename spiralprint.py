# Spiral Print
# ------------------------
# Given an N*M 2D array, print it in spiral form. That is, first you need to print the 1st row, then last column, then last row and then first column and so on.
# Print every element only once.
# Input format :
# Line 1 : N and M, No. of rows & No. of columns (separated by space) followed by N*M  elements in row wise fashion.
# Output format :
# Elements of matrix in spiral form in a single line and space separated
# Constraints :
# 0 <= N <= 10^4
# 0 <= M <= 10^4
# Sample Input 1:
#  4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# Sample Output 1:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
def spiralPrint(arr): 
    rows = len(arr) 
    cols = len(arr[0]) 
    startRow, startCol, endRow, endCol = 0, 0, rows-1, cols-1
    while startRow<=endRow and startCol<=endCol:
        # Print startRow 
        for j in range(startCol, endCol+1): 
            print(arr[startRow][j], end=' ')
        startRow += 1
        if startRow>endRow or startCol>endCol: 
            break 
        # Print endCol 
        for i in range(startRow, endRow+1): 
            print(arr[i][endCol], end=' ') 
        endCol -= 1 
        if startRow>endRow or startCol>endCol: 
            break 
        for j in range(endCol, startCol-1, -1):
            print(arr[endRow][j], end=' ')
        endRow -= 1 
        if startRow>endRow or startCol>endCol:
            break 
        # Print startCol 
        for i in range(endRow, startRow-1, -1): 
            print(arr[i][startCol], end=' ') 
        startCol += 1 
l=[int(i) for i in input().strip().split(' ')] 
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)] 
spiralPrint(arr)