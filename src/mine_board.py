from board import Board
import random

class Mine_Board(Board):

    def __init__(self, size=20, difficulty=1):
        super().__init__(size)
        self.difficulty = difficulty
        self.mine_char = u'\u2622'
        self.num_of_mines = self.determine_num_of_mines()
        self.place_mines_on_board()
        self.determine_proximity_numbers()

    def determine_num_of_mines(self):
        return round((0.075, 0.1, 0.125)[self.difficulty - 1]
                    * self.total_num_squares, 0)

# optimize this method
    def place_mines_on_board(self):
        mines = self.num_of_mines
        while mines > 0:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.board[row][col] != self.mine_char:
                self.board[row][col] = self.mine_char
                mines -= 1
# and this one
    def determine_proximity_numbers(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(self.board[row_index]):
                proximal_mines = 0
                if self.board[row_index][col_index] == self.mine_char:
                    continue
                for relative_index in self.relational_indices:
                    row_to_check = row_index + relative_index['row']
                    col_to_check = col_index + relative_index['col']
                    if not self.is_in_bounds(row_to_check, col_to_check):
                        continue
                    if self.board[row_to_check][col_to_check] == self.mine_char:
                        proximal_mines += 1
                self.board[row_index][col_index] = proximal_mines
