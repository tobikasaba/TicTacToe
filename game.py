from player import HumanPlayer, RandomComputerPlayer, GenuisComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        # use a single list to represent a 3x3 board
        self.board = [" " for _ in range(9)]
        self.current_winner = None  # keep track of winner in the game and who is it

    def print_board(self):
        board = [self.board[i * 3:(i + 1) * 3] for i in range(3)]
        for row in board:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc. (tells us what number corresponds to which spot on the box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # moves = []
        # for (index, spot_value) in enumerate(self.board):
        #     # ["x", "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")].
        #     enumerate creates a list and assigns index numbers to items in the list
        #     if spot_value == ' ':
        #         moves.append(index)
        # return moves
        moves = [index for (index, spot_value) in enumerate(
            self.board) if spot_value == " "]
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. we have to check all of these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]

        if all([spot == letter for spot in row]):
            return True

        # check the column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal

            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these fail
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter)! or None for a ti
    if print_game:
        game.print_board_nums()

    letter = "X"  # starting letter

    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate plater
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(" ")  # print an empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # after we made our move, we need to alternate letters
            letter = "O" if letter == "X" else "X"

        # adding a delay for computers response
        if print_game:
            time.sleep(0.8)

    if print_game:
        print("It\'s a tie")


if __name__ == "__main__":

    def setup_and_play(x_player_class, o_player_class, print_game=True):
        x_player = x_player_class("X")
        o_player = o_player_class("O")
        t = TicTacToe()
        return play(t, x_player, o_player, print_game=print_game)

    def two_human_players():
        return setup_and_play(HumanPlayer, HumanPlayer, print_game=True)

    def human_v_genius_computer():
        return setup_and_play(HumanPlayer, GenuisComputerPlayer, print_game=True)

    def human_v_rand_computer():
        return setup_and_play(HumanPlayer, RandomComputerPlayer, print_game=True)

    def rand_computer_v_genius_computer():
        x_wins = 0
        o_wins = 0
        ties = 0

        for i in range(1000):
            result = setup_and_play(
                RandomComputerPlayer, GenuisComputerPlayer, print_game=False)
            if result == "X":
                x_wins += 1
            elif result == "O":
                o_wins += 1
            else:
                ties += 1

        print(
            f"At the end of the game, X won {x_wins} time(s), O won {o_wins} time(s) and the game was tied {ties} time(s)")

    # two_human_players()
    # human_v_genius_computer()
    human_v_rand_computer()
    # rand_computer_v_genius_computer()