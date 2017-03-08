class Board:

    def __init__(self, size = 20):
        self.size = size
        self.board = self.create_empty_board(size)
        self.total_num_squares = size ** 2
        self.relational_indices = [
            {'row': -1, 'col': -1},
            {'row': -1, 'col': 0},
            {'row': -1, 'col': 1},
            {'row': 0, 'col': -1},
            {'row': 0, 'col': 1},
            {'row': 1, 'col': -1},
            {'row': 1, 'col': 0},
            {'row': 1, 'col': 1},
        ]

    def create_empty_board(self, size):
        return [[0 for columns in range(size)] for rows in range(size)]

    def is_in_bounds(self, row, col):
        rowInBounds = row >= 0 and row < self.size
        colInBounds = col >= 0 and col < self.size
        return rowInBounds and colInBounds
