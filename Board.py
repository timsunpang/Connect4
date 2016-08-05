from Errors import *

class Board(object):
    def __init__(self):
        self.grid = self.fill_board()
        self.full = False
        self.last_move = None

    def fill_board(self):
        board = []
        for times in range(0,8):
            board.append(Row(8, '[ ]'))
        return board

    def update(self):
        print ' ' + '   '.join(str(x) for x in range(0,8))
        for row in range(7,-1,-1):
            line = []
            for col in range(0,8):
                line.append(self.grid[col].row[row])
            print ' '.join(line)
            print

    def check_full(self):
        for row in range(len(self.grid)):
            if self.grid[row].count < 8:
                self.full = False
                return
        self.full = True
        return


    def move(self, col, player):
        self.grid[col].insert('[%s]' % player.symbol)
        self.last_move = [col, self.grid[col].count - 1]

    def valid_move(self, col):
        if col > 7 or col < 0: raise RangeError('Column number must be between 0-7')
        if self.grid[col].count >= 8: raise ColumnError('Column is already full')
        return True

    def connect_four(self):
        if self.check_horizontal(): return True
        if self.check_vertical(): return True
        if self.check_diagonal_left_right(): return True
        if self.check_diagonal_right_left(): return True
        return False

    def check_horizontal(self):
        row = self.last_move[0]
        col = self.last_move[1]
        value = self.grid[row].row[col]
        counter = 0

        for idx in range(-3,4):
            if self.in_range(col + idx):
                if self.grid[row].row[col + idx] == value:
                    counter += 1
                else:
                    counter = 0
            if counter >= 4: return True

        return False

    def check_vertical(self):
        row = self.last_move[0]
        col = self.last_move[1]
        value = self.grid[row].row[col]
        counter = 0

        for idx in range(-3, 4):
            if self.in_range(row + idx):
                if self.grid[row + idx].row[col] == value:
                    counter += 1
                else:
                    counter = 0
            if counter >= 4: return True

        return False

    def check_diagonal_left_right(self):
        row = self.last_move[0]
        col = self.last_move[1]
        value = self.grid[row].row[col]
        counter = 0

        for idx in range(-3, 4):
            if self.in_range(row + idx) and self.in_range(col + idx):
                if self.grid[row + idx].row[col + idx] == value:
                    counter += 1
                else:
                    counter = 0
            if counter >= 4: return True

        return False

    def check_diagonal_right_left(self):
        row = self.last_move[0]
        col = self.last_move[1]
        value = self.grid[row].row[col]
        counter = 0

        for idx in range(-3, 4):
            if self.in_range(row + idx) and self.in_range(col - idx):
                if self.grid[row + idx].row[col - idx] == value:
                    counter += 1
                else:
                    counter = 0
            if counter >= 4: return True

        return False

    def in_range(self, num):
        return num >= 0 and num <= 7

class Row(object):
    def __init__(self, length, default_value):
        self.row = [default_value] * length
        self.count = 0
        self.default_value = default_value
    def insert(self, val):
        self.row[self.count] = val
        self.count += 1
    def delete_last(self):
        self.row[self.count - 1] = default_value
