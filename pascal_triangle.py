def pascal_recursive(row, col):
    if col == 0 or col == row:
        return 1
    return pascal_recursive(row - 1, col - 1) + pascal_recursive(row - 1, col)

def print_pascals_triangle(n):
    for row in range(n):
        print(' ' * (n - row), end='')  # spacing for pyramid shape
        for col in range(row + 1):
            print(pascal_recursive(row, col), end=' ')
        print()


rows = int(input("Enter number of rows: "))
print_pascals_triangle(rows)
