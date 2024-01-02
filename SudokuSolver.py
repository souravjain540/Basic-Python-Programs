import cowsay
import sys
import re

def find_next_empty(puzzle):
    # Finds the next row, col on the puzzle that is not filled yet --> rep with -1
    # Return row, col tuple(or (None, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None

def is_valid(puzzle, guess, row, col):
    # Figures out whether the guess at the row/col of the puzzle is a valid guess
    # Returns True if is valid, False otherwise

    # Row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # Pass
    return True

def solve_sudoku(puzzle):
    """
    Solve sudoku using backtracking!
    The puzzle is a list of lists, where each inner list is a row in the sudoku puzzle
    Return whether a solution exists
    Mutates puzzle to be the solution (if solution exists)
    """

    # Step 1: Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: If there is nowhere left, the program has finished because only valid inputs are allowed
    if row is None:
        return True

    # Step 2: If there is a place to put a number, make a guess between 1 and 9
    for guess in range(1, 10):
        # Step 3: Check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: Place that guess on the puzzle!
            puzzle[row][col] = guess
            # Recurse using this puzzle!
            # Step 4: Recursively call the function
            if solve_sudoku(puzzle):
                return True

        # Step 5: if not valid OR guess does not solve the puzzle, backtrack and try a new number
        puzzle[row][col] = -1   # Reset the guess

    # Step 6: if none of the numbers work, the puzzle is UNSOLVABLE
    return False

def print_sudoku(puzzle):
    # Print a(n) (un-) solved sudoku

    for r in range(9):
        for c in range(9):
            # Use an empty space in front of numbers unequal -1 to keep the format
            if puzzle[r][c] != -1:
                start_string = " "
            else:
                # Use no empty space in front -1 to keep the format
                start_string = ""
            if c == 3 or c == 6:
                # Print | when starting a new square
                print("|" + start_string + str(puzzle[r][c]), end=" ")
            else:
                print(start_string + str(puzzle[r][c]), end=" ")

        # Start a new row
        print("")
        # Separate the squares
        if r == 2 or r == 5:
            print("---------+---------+---------")

def user_demonstration():
    # Demonstrate the program using an example board
    # The example board:
    example_board = [
        [ 3, 9,-1,    -1, 5,-1,    -1,-1,-1],
        [-1,-1,-1,     2,-1,-1,    -1,-1, 5],
        [-1,-1,-1,     7, 1, 9,    -1, 8,-1],

        [-1, 5,-1,    -1, 6, 8,    -1,-1,-1],
        [ 2,-1, 6,    -1,-1, 3,    -1,-1,-1],
        [-1,-1,-1,    -1,-1,-1,    -1,-1, 4],

        [ 5,-1,-1,    -1,-1,-1,    -1,-1,-1],
        [ 6, 7,-1,     1,-1, 5,    -1, 4,-1],
        [ 1,-1, 9,    -1,-1,-1,     2,-1,-1],
    ]

    # Print the unsolved example board
    print("\nExample board unsolved:")
    print_sudoku(example_board)

    # Solve the example board
    solve_sudoku(example_board)

    # Print the solved example board
    print("\nExample board solved:")
    print_sudoku(example_board)
    print("")

def get_user_puzzle():
    # Prompt the user for his own puzzle
    # Return the user's puzzle

    # Give instructions to the user
    print("Enter your own sudoku row by row. For empty cells, type '-1'. After entering a row, hit enter. Make sure you enter exact 9 numbers.")

    # Get the user's sudoku
    puzzle = []
    for i in range(9):
        # Get the row
        row_input = input(f"Row {i}: ")
        # Format the row
        row_input = re.sub(r"\s", "", row_input)
        # Create the row
        try:
            row = []
            i = 0
            while i < len(row_input):
                if row_input[i] == "-":
                    row.append(int(row_input[i:i+2]))
                    i += 2
                else:
                    row.append(int(row_input[i]))
                    i += 1
        except:
            print("Invalid input")
            break

        # Check if 9 numbers have been enterd
        if len(row) != 9:
            print("Invalid input")
            break

        print(row)
        puzzle.append(row)

    return puzzle

def main():
    # Navigate through the program using the command line
    # Press 'd' for a demonstration of the program using an exmaple board
    # Press 'e' to enter your own puzzle row by row
    # Press 'q' to quit the program

    # Greet the user an explain the program
    greeting = "WELCOME TO THE SUDOKU SOLVER!\n"\
               "Press 'd' for a demonstration of the program using an exmaple board\n"\
               "Press 'e' to enter your own puzzle row by row\n"\
               "Press 'q' to quit the program\n"
    cowsay.cow(greeting)
    print("")

    while True:
        # Get the user input
        user_input = input("Enter: ")
        if user_input == "d":
            # Demonstrate the program
            user_demonstration()
        elif user_input == "e":
            # Solve an user specific sudoku
            # Get and print the user's puzzle
            puzzle = get_user_puzzle()
            print("\nUnsolved sudoku:")
            print_sudoku(puzzle)

            # Solve and print the solved puzzle
            solve_sudoku(puzzle)
            print("\nSolved sudoku")
            print_sudoku(puzzle)
        elif user_input == "q":
            sys.exit("See you soon...")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
    