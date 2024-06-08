import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # game is an instance of TicTacToe passed from play() function.
        # as long as the method is called on instances of TicTacToe
        # which have access to the available_moves function/method, this won't throw an error
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


class GenuisComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # computer selects a random spot
            square = random.choice(game.available_moves())
        else:
            # get a square (position) based off the minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = "O" if player == "X" else "X"  # the other player

        # first we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep track of the score
            # for minimax to work
            return {"position": None,
                    "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():  # no empty squares
            return {"position": None, "score": 0}

        if player == max_player:
            # each score should be maximised (be larger)
            best = {"position": None, "score": -math.inf}
        else:
            # each score should minimise
            best = {"position": None, "score": math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # step 2: recurse using minimax to simulate a game after making that move
            # now we alternate players
            sim_score = self.minimax(state, other_player)

            # step 3: undo the move
            state.board[possible_move] = " "
            state.current_winner = None

            # otherwise this will get messed up from recursion
            sim_score["position"] = possible_move

            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score  # replace best
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score  # replace best

        return best
