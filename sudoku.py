sudoku = input("Enter Soduku(without any space and assume empty space as 0): ")
#INPUT: 250030901010004000407000208005200000000098100040003000000360072070000003903000604
puz = [[int(sudoku[(i+j)-1]) for i in range(1,10)] for j in range(0,81,9)]


def check(puzzle, i, row, col):
    rows = puzzle[int(row)]
    column = [puzzle[r][col] for r in range(0,9,1)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3)*3
    squareColumn = (col // 3)*3
    Square = [puzzle[y][z] for y in range(SquareRow, SquareRow+3) for z in range(squareColumn, squareColumn+3)]
    if i in Square:
        return False
    return True


def find(puzzle):
    for i in range(0,9,1):
        for j in range(0,9,1):
            if puzzle[i][j]==0:
                return i,j
    return None


def solve(board):
    finds = find(board)
    if not finds:
        return True
    else:
        row, col = finds

    for i in range(1,10):
        if check(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print(solve(puz))
print(puz)

# OUTPUT: True 
# [[2, 5, 8, 7, 3, 6, 9, 4, 1], [6, 1, 9, 8, 2, 4, 3, 5, 7], [4, 3, 7, 9, 1, 5, 2, 6, 8], [3, 9, 5, 2, 7, 1, 4, 8, 6], [7, 6, 2, 4, 9, 8, 1, 3, 5], [8, 4, 1, 6, 5, 3, 7, 2, 9], [1, 8, 4, 3, 6, 9, 5, 7, 2], [5, 7, 6, 1, 4, 2, 8, 9, 3], [9, 2, 3, 5, 8, 7, 6, 1, 4]]