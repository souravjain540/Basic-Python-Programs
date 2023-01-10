import math
import random


class Player():
    def __init__(self, player):
        self.player = player

    def get_move(self, game):
        pass


class Human(Player):
    def __init__(self, player):
        super().__init__(player)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.player + ' turn. Please introduce a move (1-9): ')
            try:
                val = int(square) - 1
                if val not in game.remaining_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputer(Player):
    def __init__(self, player):
        super().__init__(player)

    def get_move(self, game):
        square = random.choice(game.remaining_moves())
        return square


class SmartComputer(Player):
    def __init__(self, player):
        super().__init__(player)

    def get_move(self, game):
        if len(game.remaining_moves()) == 9:
            square = random.choice(game.remaining_moves())
        else:
            square = self.minimax(game, self.player)['position']
        return square

    def minimax(self, state, player):
        max_player = self.player
        min_player = '0' if player == 'X' else 'X'

        # checking if the previous move is winner
        if state.actual_winner == min_player:
            return {'position': None,
                    'score': 1 * (state.number_null_squares() + 1) if min_player == max_player
                    else -1 * (state.number_null_squares() + 1)}
        elif not state.null_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.remaining_moves():
            state.make_a_move(possible_move, player)
            sim_score = self.minimax(state, min_player)

            # undo move
            state.board[possible_move] = ' '
            state.actual_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
