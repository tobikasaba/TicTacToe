import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomeComuterPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # game is an instance of TicTacToe passed from play() function.
        # as long as the method is called on insatnces of TicTacToe
        # which have access to the available_moves function/method, this wont throw an error
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move 0-8):")
        # we're going to check that this is a correct value by trying to cast
        # it to an integer, and if it's not, then we say its invalid
        # if that spot is not available on the board, we also say its invalid
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return value
