import sys
import pygame
from maze_example import maze_generator


#initialize pygame
pygame.init()
sys.setrecursionlimit(100000)

FPS = 120

SIZE_BLOCK = 10

WIDTH = None
HEIGHT = None

YELLOW = (251, 255, 65)
GREEN = (96, 189, 4)
BLUE = (0, 195, 255)
RED = (201, 0, 0)
PURPLE = (216, 26, 240)

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)
moves = [DOWN, LEFT, UP, RIGHT]


def draw_single_block(state, color):
    r = pygame.Rect((state.get_position()[1]*SIZE_BLOCK, state.get_position()[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
    pygame.draw.rect(screen, color, r)


def draw_trail(cc, color):
    r = pygame.Rect((cc[1]*SIZE_BLOCK, cc[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
    pygame.draw.rect(screen, color, r)


class Node(object):
    """docstring for Node."""

    def __init__(self, position, prev):

        self.position = position
        self.prev = prev


    def get_position(self):

        return self.position


    def get_prev(self):

        return self.prev


    def go_back_to(self, c, cc_returning_list):

        if self.prev == c:
            cc_returning_list.append(self.prev)
            print(f"Returned to {self.prev.get_position()}")
            return None
        else:
            cc_returning_list.append(self.prev)
            self.get_prev().go_back_to(c, cc_returning_list)


    def get_solution(self, initial, cc_returning_list):

        if self == initial:
            cc_returning_list.append(self)
            print(f"Returned to {self.get_position()}")
            return None
        else:
            cc_returning_list.append(self)
            self.get_prev().get_solution(initial, cc_returning_list)


class Player(object):
    """docstring for player."""

    def __init__(self, node):
        self.node_state = node

    def get_state(self):
        return self.node_state

    def get_position(self):
        return self.node_state.get_position()

    def draw(self, screen):
        r = pygame.Rect((self.get_position()[1]*SIZE_BLOCK, self.get_position()[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
        pygame.draw.rect(screen, YELLOW, r)

    def move(self, temp_pos):
        self.node_state = temp_pos
        print(f"current player position: {self.get_position()}")


class Maze():

    def __init__(self):
        self.spaces = []
        self.node_queue = []
        self.record = []
        self.end = []

    def left_pop(self):
        return self.queue.pop(0)

    def get_spaces(self):
        return self.spaces

    def get_record(self):
        return self.record

    def can_move(self, player, move, current):
        temp_pos = Node((player.get_position()[0]+move[0], player.get_position()[1]+move[1]), current)
        if (temp_pos.get_position() in self.spaces) and not (temp_pos.get_position() in self.record):
            return temp_pos

    def finished(self, pos):
        return self.end[0] == pos

    def depth_first_search(self, node_succesors):
        while len(node_succesors) > 0:
            self.node_queue.insert(0, node_succesors.pop())

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

    initial = None
    current = None
    last = None
    returning = False
    checkpoints = []
    node_succesors = []
    succesors = []
    cc_returning_list = []

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
                initial = Node((f,c), None)
                player = Player(initial)
                current = initial
                last = current
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

        if not maze.finished(player.get_position()):

            #Logic
            if not returning:
                n = 0

                for move in moves:
                    aux = maze.can_move(player, move, current)
                    if aux:
                        node_succesors.append(aux)
                        n += 1

                maze.depth_first_search(node_succesors)

                if n > 1:
                    for _ in range(n-1):
                        checkpoints.append(player.get_state())
                    print(f"checkpoint at {checkpoints[-1].get_position()}")
                elif n == 0:
                    current.go_back_to(checkpoints[-1], cc_returning_list)
                    returning = True
                    continue

                current = maze.node_queue.pop(0)
                player.move(current)
                maze.record.append(current.get_position())

            else:
                if len(cc_returning_list)>0:
                    current = cc_returning_list.pop(0)
                    player.move(current)
                else:
                    checkpoints.pop()
                    current = maze.node_queue.pop(0)
                    player.move(current)
                    maze.record.append(current.get_position())
                    returning = False

            #Visual
            draw_single_block(last, BLUE)
            if len(checkpoints)>0: draw_single_block(checkpoints[-1], PURPLE)
            player.draw(screen)

            last = current

        else:
            if not returning:
                current.get_solution(initial, cc_returning_list)
                returning = True
            elif returning and len(cc_returning_list)>0:
                FPS = 144/2
                draw_single_block(cc_returning_list.pop(0), GREEN)
            else:
                FPS = 1
                print("Finish")
                run = False

        clock.tick(FPS)
        pygame.display.update()
