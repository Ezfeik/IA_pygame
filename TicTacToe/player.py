import pygame
from search import Search

class Player():

    def __init__(self, l, ia):
        self.letter = l
        self.ia = ia


    def get_letter(self):
        return self.letter


    def turn(self, board, pos, opponent):
        if self.ia:
            search = Search(board.get_matrix(), opponent.get_letter())
            board.set_letter(search.find(), self.letter)
            return True
        else:
            if pos == None:
                return False
            elif board.matrix[pos[0]][pos[1]] == " ":
                board.set_letter(pos[0], pos[1], self.letter)
                return True
            else:
                return False
