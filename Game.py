from Board import *
from Player import *
# from Errors import *

class Game(object):
    def __init__(self):
        self.board = Board()
        self.player_1 = Player('x', self.board)
        self.player_2 = Player('o', self.board)
        self.game_over = False
        self.current_player = self.player_1

    def play(self):
        while not self.game_over:
            self.take_turn()
            if self.game_over: break
            self.switch_player()
        self.board.update()
        if self.player_1.winner:
            print "Player 1 wins!"
            return
        if self.player_2.winner:
            print "Player 2 wins!"
            return
        print "No winner."
        return

    def take_turn(self):
        self.board.update()
        if self.current_player == self.player_1:
            print "Player 1's turn"
        else:
            print "Player 2's turn"
        self.current_player.make_move()
        self.board.check_full()
        if self.board.connect_four():
            self.current_player.winner = True
            self.game_over = True
        if self.board.full:
            self.game_over = True


    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

if __name__ == '__main__':
    game = Game()
    game.play()
