class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        board = [self.board[i*3:(i+1*3)] for i in range(3)]
        for row in board:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def prit_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # moves = []
        # for (index, spot_value) in enumerate(self.board):
        #     # ["x", "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")]
        #     if spot_value == ' ':
        #         moves.append(index)
        # return moves
        moves = [index for (index, spot_value) in enumerate(
            self.board) if spot_value == " "]
        return moves
