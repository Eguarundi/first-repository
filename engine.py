import numpy as np

from board import HexBoard

class HexEngine:
    def __init__(self, board, seed=33):
        self.b = board
        self.rng = np.random.default_rng(seed=seed)

    def make_random_move(self):
        moves = self.possible_moves()
        row, col = self.rng.choice(moves)
        self.b.make_move(row, col)

    def possible_moves(self):
        return np.column_stack(np.nonzero(self.b.cells == 0))

board = HexBoard(5)
heng = HexEngine(board)
for _ in range(25):
    heng.make_random_move()
    board.print()

print(board.is_blue_win())
