import sys, pygame
from maze_example import maze_generator

#initialize pygame
pygame.init()

SIZE_BLOCK = 4

WIDTH = 420
HEIGHT = 420

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
moves = [UP, DOWN, LEFT, RIGHT]


class Player(object):
    """docstring for player."""

    def __init__(self, pos):
        self.position = pos
        pass

    def get_position(self):
        return self.position

    def draw(self, screen):
        r = pygame.Rect((self.position[1]*SIZE_BLOCK, self.position[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
        pygame.draw.rect(screen, (0, 195, 255), r)

    def move(self, temp_pos, maze):
        self.position = temp_pos
        maze.record.append(temp_pos)
        print(f"current player position: {self.position}")


class Maze():

    def __init__(self):
        self.spaces = []
        self.queue = []
        self.record = []
        self.end = []

    def left_pop(self):
        return self.queue.pop(0)

    def get_spaces(self):
        return self.spaces

    def get_record(self):
        return self.record

    def can_move(self, player, move):
        temp_pos = (player.position[0]+move[0], player.position[1]+move[1])
        if (temp_pos in self.spaces) and not (temp_pos in self.record):
            return temp_pos

    def finished(self, pos):
        return self.end[0] == pos

    def depth_first_search(self, sucesors):
        while len(sucesors) > 0:
            self.queue.insert(0,sucesors.pop())

    def breadth_first_search(self, sucesors):
        while len(sucesors) > 0:
            self.queue.append(sucesors.pop(0))

    def draw(self, screen, maze_map):
        for f in range(0,NUM_BLOCKS_H):
            for c in range(0,NUM_BLOCKS_W):
                if maze_map[f][c] == "1":
                    r1 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                    pygame.draw.rect(screen, (23, 23, 23), r1)
                elif maze_map[f][c] == "0" or maze_map[f][c] == "I":
                    r2 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                    pygame.draw.rect(screen, (233, 233, 233), r2)
                elif maze_map[f][c] == "F":
                    r3 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                    pygame.draw.rect(screen, (201, 0, 0), r3)


if __name__ == '__main__':

    #Datos Iniciales

    maze_map = maze_generator().split('\n')
    WIDTH = int(len(maze_map[0])*SIZE_BLOCK)
    HEIGHT = int(len(maze_map)*SIZE_BLOCK)
    NUM_BLOCKS_W = int(WIDTH/SIZE_BLOCK)
    NUM_BLOCKS_H = int(HEIGHT/SIZE_BLOCK)

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    maze = Maze()

    sucesors = []

    for f in range(0,NUM_BLOCKS_H):
        for c in range(0,NUM_BLOCKS_W):
            if maze_map[f][c] == "1":
                r1 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                pygame.draw.rect(screen, (23, 23, 23), r1)
            elif maze_map[f][c] == "0":
                r2 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                pygame.draw.rect(screen, (233, 233, 233), r2)
                maze.spaces.append((f,c))
            elif maze_map[f][c] == "F":
                r3 = pygame.Rect((c*SIZE_BLOCK, f*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
                pygame.draw.rect(screen, (201, 0, 0), r3)
                maze.spaces.append((f,c))
                maze.end.append((f,c))
            elif maze_map[f][c] == "I":
                player = Player((f,c))
                print(f"start position: {player.get_position()}")
                maze.record.append((f,c))
                maze.spaces.append((f,c))

    maze.draw(screen, maze_map)
    player.draw(screen)
    pygame.display.update()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for move in moves:
            aux = maze.can_move(player, move)
            if aux:
                sucesors.append(maze.can_move(player, move))

        maze.depth_first_search(sucesors)
        # maze.breadth_first_search(sucesors)

        if maze.finished(player.position):
            clock.tick(1)
            print("Finish")
            run = False
            break

        # maze.draw(screen, maze_map)

        player.move(maze.left_pop(), maze)
        player.draw(screen)
        clock.tick(2)

        pygame.display.update()
