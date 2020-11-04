import pygame


class Board():

    def __init__(self, gs):
        self.matrix = [[" " for _ in range(3)] for _ in range(3)]
        self.color = (0,0,0)
        self.grid_size = gs


    def set_matrix(self, m):
        self.matrix = m


    def set_letter(self, i, j, l):
        self.matrix[i][j] = l


    def get_matrix(self):
        return self.matrix


    def game_over(self):
        for i in range(3):
            if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] != " ":
                return True
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] != " ":
                return True
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != " ":
            return True
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != " ":
            return True

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
