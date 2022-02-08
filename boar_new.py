import numpy as np


class HexBoard:
    def __init__(self, size):
        self.size = size
        self.cells = np.zeros((size, size), dtype=int)
        self.nmoves = 0

    def is_valid_coordinates(self, row, col):
        assert row >= 0 and row < self.size and col >= 0 and col < self.size

    def is_valid_coordinates_2(self, row, col):
        return row >= 0 and row < self.size and col >= 0 and col < self.size

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

    def is_blue_win(self):
        stack = [(0, i) for i in range(self.size) if self.cells[0, i] == 1]
        visited = set()

        while len(stack) > 0:
            curcell = stack.pop()
            visited.add(curcell)
            if curcell[0] == self.size - 1:
                return True

            for neib in self.neighbours(curcell):
                if neib not in visited:
                    stack.append(neib)

        return False

    def neighbours(self, curcell):
        N = []
        if self.is_valid_coordinates_2(curcell[0], curcell[1]+1) and self.cells[curcell[0]][curcell[1]+1] == 1:  # правая
            N.append((curcell[0], curcell[1]+1))
        if self.is_valid_coordinates_2(curcell[0], curcell[1]-1) and self.cells[curcell[0]][curcell[1]-1] == 1:  # левая
            N.append((curcell[0], curcell[1]-1))
        if self.is_valid_coordinates_2(curcell[0]+1, curcell[1]) and self.cells[curcell[0]+1, curcell[1]] == 1:
            N.append((curcell[0]+1, curcell[1]))
        if self.is_valid_coordinates_2(curcell[0]-1, curcell[1]) and self.cells[curcell[0]-1, curcell[1]] == 1:
            N.append((curcell[0]-1, curcell[1]))
        if self.is_valid_coordinates_2(curcell[0]+1, curcell[1]-1) and self.cells[curcell[0]+1, curcell[1]-1] == 1:
            N.append((curcell[0]+1, curcell[1]-1))
        if self.is_valid_coordinates_2(curcell[0]-1, curcell[1]+1) and self.cells[curcell[0]-1, curcell[1]+1] == 1:
            N.append((curcell[0]-1, curcell[1]+1))
        # N.append((curcell[0], curcell[1]+1) if self.cells[curcell[0]][curcell[1]+1] == 1)
        return N



    def is_red_win(self):
        B = [ (i, 0) for i in self.size if self.cells(i, 0) == 2]
        visited = set()

        while len(B) > 0:
            curcell = B.pop()
            visited.add(curcell)
            if curcell[0] == self.size - 1:
                return True
            for b in self.neighbours(curcell):
                if b not in visited:
                    B.append(b)
        return False

board = HexBoard(5)
# print(type(board))
# print(board.cells)
# print(board.cells.shape)

board.print()
board.make_move(2, 0)
board.make_move(0, 3)
board.make_move(1, 4)
board.make_move(0, 4)
board.print()
board.is_blue_win()