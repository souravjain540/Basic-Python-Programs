board = [[' ' for _ in range(3)] for _ in range(3)]

def checkwinner(a):
    if (board[0][0] == a and board[1][0] == a and board[2][0] == a or
        board[0][1] == a and board[1][1] == a and board[2][1] == a or
        board[0][2] == a and board[1][2] == a and board[2][2] == a):
        return 1
    elif (board[0][0] == a and board[0][1] == a and board[0][2] == a or
          board[1][0] == a and board[1][1] == a and board[1][2] == a or
          board[2][0] == a and board[2][1] == a and board[2][2] == a):
        return 1
    elif (board[0][0] == a and board[1][1] == a and board[2][2] == a or
          board[0][2] == a and board[1][1] == a and board[2][0] == a):
        return 1
    else:
        return 0

def fill():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '

def play(box, a):
    row = (box - 1) // 3
    col = (box - 1) % 3
    if board[row][col] != ' ':
        return 1
    else:
        board[row][col] = a
        return 0

def display():
    print(f"\n {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

print("\nWelcome to Tic Tac Toe\n")
print(" 1 | 2 | 3 ")
print("---|---|---")
print(" 4 | 5 | 6 ")
print("---|---|---")
print(" 7 | 8 | 9 ")

while True:
    fill()
    instruction = input("\n\n1. Press Enter to start a new game.\n2. Press E to exit.\n-->")

    if instruction == "":
        count = 0
        result = 0

        while not result and count < 9:
            if count % 2 == 0:
                cell = int(input("\n\nEnter the number to mark (O):  "))
                if 1 <= cell <= 9:
                    if play(cell, 'O'):
                        print("\nBlock already filled")
                        continue
                    else:
                        play(cell, 'O')
                        display()
                        count += 1

                    if checkwinner('O'):
                        print("\n\nCongratulations O won!!!\n")
                        result = 1
                    else:
                        continue
                else:
                    print("\nInvalid Input")
                    continue
            else:
                cell = int(input("\n\nEnter the number to mark (X):  "))
                if 1 <= cell <= 9:
                    if play(cell, 'X'):
                        print("\nBlock already filled")
                        continue
                    else:
                        play(cell, 'X')
                        display()
                        count += 1

                    if checkwinner('X'):
                        print("\n\nCongratulations X won!!!\n")
                        result = 1
                    else:
                        continue
                else:
                    print("\nInvalid Input")
                    continue

            if not result and count == 9:
                print("\n\nIt is a DRAW!!")

    elif instruction.lower() == 'e':
        print("\nThanks for Playing!")
        print("------------------------------")
        break
