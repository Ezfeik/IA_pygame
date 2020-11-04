import pygame


class Board():

    def __init__(self, gs):
        self.matrix = [[" " for _ in range(3)] for _ in range(3)]
        self.color = (0,0,0)
        self.grid_size = gs


    def set_matrix(self, i, j, l):
        self.matrix[i][j] = l


    def game_over(self):
        if self.matrix[0][0] == self.matrix[0][1] == self.matrix[0][2] != " ":
            return True
        elif self.matrix[1][0] == self.matrix[1][1] == self.matrix[1][2] != " ":
            return True
        elif self.matrix[2][0] == self.matrix[2][1] == self.matrix[2][2] != " ":
            return True
        elif self.matrix[0][0] == self.matrix[1][0] == self.matrix[2][0] != " ":
            return True
        elif self.matrix[0][1] == self.matrix[1][1] == self.matrix[2][1] != " ":
            return True
        elif self.matrix[0][2] == self.matrix[1][2] == self.matrix[2][2] != " ":
            return True
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != " ":
            return True
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != " ":
            return True
        else:
            return False


    def draw(self, screen):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, self.color, ((i*self.grid_size, j*self.grid_size), (self.grid_size, self.grid_size)), 3)

        for i in range(3):
            for j in range(3):
                font = pygame.font.Font('freesansbold.ttf', 150)
                text = font.render(self.matrix[i][j], True, self.color)
                screen.blit(text, ((j*self.grid_size + 30, i*self.grid_size + 15), (self.grid_size, self.grid_size)))
