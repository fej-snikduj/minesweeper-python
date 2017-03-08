from mine_board import Mine_Board
from helpers import list_to_string
import json

class View_Board(Mine_Board):
    def __init__(self, size=20, difficulty=1):
        super().__init__(size, difficulty)

        self.cursor_char = u'\u25AB'
        self.marker_char = u'\u2733'
        self.uncovered_space_char = ' '
        self.covered_space_char = u'\u2B1C'

        self.view_board = self.generate_view_board()
        self.uncovered_count = 0
        self.winning_uncovered_count = (self.total_num_squares
                                        - self.num_of_mines)
        self.row = 0
        self.col = 0
        self.game_over = False

    def generate_view_board(self):
        return [
                [self.covered_space_char for x in range(self.size)]
                for y in range(self.size)
        ]

    def print_view_board(self, show_cursor = True):
        self.clear_console()
        # make a copy of the view board so that you can temporarily mutate it
        board_to_print = json.loads(json.dumps(self.view_board))
        # cursor is only shown after changing cursor location
        if show_cursor:
            board_to_print[self.row][self.col] = self.cursor_char

        for row in board_to_print:
            print(list_to_string(row, ' '))

    def move_cursor(self, direction):
        new_row = self.row
        new_col = self.col
        if direction == 'up':
            new_row = new_row - 1
        elif direction =='down':
            new_row = new_row + 1
        elif direction == 'right':
            new_col = new_col + 1
        elif direction == 'left':
            new_col = new_col - 1
        else:
            return
        if self.is_in_bounds(new_row, new_col):
            self.row = new_row
            self.col = new_col
            self.print_view_board(True)

    def mark_space(self):
        if self.view_board[self.row][self.col] == self.covered_space_char:
            self.view_board[self.row][self.col] = self.marker_char
        elif self.view_board[self.row][self.col] == self.marker_char:
            self.view_board[self.row][self.col] = self.covered_space_char
        self.print_view_board(False)


    def clear_console(self):
        print('\x1B[2J')



x = View_Board(5,3)
x.move_cursor('right')
x.move_cursor('up')
x.move_cursor('down')
x.mark_space()
x.move_cursor('right')
