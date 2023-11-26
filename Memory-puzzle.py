import random

def generate_board(size=4):
    if size % 2 != 0:
        raise ValueError("Size must be even")

    letters = [chr(i) for i in range(65, 65 + (size * size // 2))]
    board = letters + letters
    random.shuffle(board)
    return [board[i:i + size] for i in range(0, len(board), size)]

def print_board(board, revealed):
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if revealed[row_idx][col_idx]:
                print(cell, end=' ')
            else:
                print('_', end=' ')
        print()

def get_choice(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (e.g. '1 2'): ").split())
            if row >= 1 and row <= len(board) and col >= 1 and col <= len(board[0]):
                return row - 1, col - 1
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter row and column numbers separated by space.")

def memory_puzzle():
    board = generate_board()
    revealed = [[False] * len(board) for _ in range(len(board))]

    moves = 0
    while not all(all(row) for row in revealed):
        print_board(board, revealed)
        print("Choose the first card to flip.")
        row1, col1 = get_choice(board)

        revealed[row1][col1] = True
        print_board(board, revealed)
        print("Choose the second card to flip.")
        row2, col2 = get_choice(board)

        if (row1, col1) == (row2, col2):
            print("You chose the same card. Choose a different second card.")
            continue

        revealed[row2][col2] = True
        print_board(board, revealed)

        if board[row1][col1] != board[row2][col2]:
            print("Not a match.")
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        else:
            print("It's a match!")

        moves += 1

    print(f"Congratulations! You completed the game in {moves} moves.")

if __name__ == "__main__":
    memory_puzzle()
