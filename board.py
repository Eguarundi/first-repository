import numpy as np


class HexBoard:
    def __init__(self, size):
        self.size = size
        self.cells = np.zeros((size, size), dtype=int)
        self.nmoves = 0

    def is_valid_coordinates(self, row, col):
        assert row >= 0 and row < self.size and col >= 0 and col < self.size

    def make_move(self, row, col):
        self.is_valid_coordinates(row, col)
        if self.cells[row, col] != 0:
            print('Cell is occuped')
            return
        self.cells[row, col] = 1 if self.nmoves % 2 else 2
        self.nmoves += 1

    def print(self):
        horizontal_line = '-' * (self.size * 3 + 3)
        print(horizontal_line)
        for row in range(self.size):
            pref = '  ' * row
            print(pref + ' \ '.join([str(item) for item in self.cells[row]]))
            print(pref + horizontal_line)

board = HexBoard(5)
print(type(board))
print(board.cells)
print(board.cells.shape)

board.print()
board.make_move(2, 3)
board.make_move(1, 3)
board.print()
