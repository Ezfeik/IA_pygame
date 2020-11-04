import pygame
import random


class Player():

    def __init__(self, l, ia):
        self.letter = l
        self.ia = ia

    def turn(self, board, pos):
        if self.ia:
            pos_ia = random.randint(0,2), random.randint(0,2)
            if board.matrix[pos_ia[0]][pos_ia[1]] == " ":
                board.set_matrix(pos_ia[0], pos_ia[1], self.letter)
                print("Coloque una ", self.letter)
                return True
            else:
                return False
        else:
            if pos == None:
                return False
            elif board.matrix[pos[0]][pos[1]] == " ":
                board.set_matrix(pos[0], pos[1], self.letter)
                print("Coloque una ", self.letter)
                return True
            else:
                return False

    def draw(self):
        pass
