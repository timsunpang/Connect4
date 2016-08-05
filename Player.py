from Errors import *

class Player(object):
    def __init__(self, symbol, board):
        self.symbol = symbol
        self.winner = False
        self.board = board

    def make_move(self):
        while True:
            try:
                column = int(input('Select a column 0-7: '))
                if self.board.valid_move(column):
                    self.board.move(column, self)
                    break
            except (RangeError, ColumnError) as e:
                print(e.value)
                print("Try again.")
