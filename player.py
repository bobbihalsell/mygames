import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass 

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass 

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # get rows like [' ', ' ', ' ']
            print('| ' + ' | '.join(row) + ' |') # create board

    def print_board_nums():
        num_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in num_board: # get rows like ['0', '1', '2']
            print('| ' + ' | '.join(row) + ' |')


