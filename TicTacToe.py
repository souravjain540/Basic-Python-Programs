import math
import time
from Player import SmartComputer, RandomComputer, Human


class TicTacToe():
    def __init__(self):
        self.board = self.create_board()
        self.actual_winner = None

    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]

    def board_show(self):
        for cell in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(cell) + ' |')

    @staticmethod
    def show_board_numbers():
        number_from_board = [[str(i + 1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for cell in number_from_board:
            print('| ' + ' | '.join(cell) + ' |')

    def make_a_move(self, square, player):
        if self.board[square] == ' ':
            self.board[square] = player
            if self.winner_rules(square, player):
                self.actual_winner = player
            return True
        return False

    def winner_rules(self, square, player):
        # Checking the row
        row_index = math.floor(square / 3)
        row = self.board[row_index*3:(row_index+1)*3]
        if all([l == player for l in row]):
            return True

        # Checking the column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([l == player for l in column]):
            return True

        # Checking for diagonal
        if square % 2 == 0:
            principal_diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([l == player for l in principal_diagonal]):
                return True

            secondary_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([l == player for l in secondary_diagonal]):
                return True

        return False

    def null_squares(self):
        return ' ' in self.board

    def number_null_squares(self):
        return self.board.count(' ')

    def remaining_moves(self):
        return [p for p, i in enumerate(self.board) if i == ' ']


def play(game, x_player, o_player, show_game = True):
    if show_game:
        game.show_board_numbers()

    player = 'X'
    while game.null_squares():
        if player == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_a_move(square, player):
            if show_game:
                print(f'{player} makes a move to square {square}')
                game.board_show()
                print(' ')

            if game.actual_winner:
                if show_game:
                    print(f'{player} wins!')
                return player
            player = '0' if player == 'X' else 'X'

        time.sleep(.8)

    if show_game:
        print('Tie!')


if __name__ == '__main__':
    #x_player = RandomComputer('0')
    x_player = SmartComputer('0')
    o_player = Human('X')
    t = TicTacToe()
    play(t, o_player, x_player, True)



