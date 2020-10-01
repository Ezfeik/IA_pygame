import sys, pygame
from maze_example import maze_generator

sys.setrecursionlimit(100000)

#initialize pygame
pygame.init()

WIDTH = None
HEIGHT = None

SIZE_BLOCK = 20

UP = (-1,0,"UP")
DOWN = (1,0,"DOWN")
LEFT = (0,-1,"LEFT")
RIGHT = (0,1,"RIGHT")
moves = [UP, DOWN, LEFT, RIGHT]


class State():
    def __init__(self, position, origin):
        self.position = position
        self.origin = origin

    def __eq__(self, e):
        return self.position == e.position

    def imprimir(self):
        return f"Posicion: {self.position} Origen: {self.origin}"

    def get_position(self):
        return self.position

    def get_origin(self):
        return self.origin

    def search_origin(self, state):
        if self.origin == state:
            pass
        else:
            self.buscar_padre(e.get_padre())
            print("\n" + e.get_accion() + "\n Nivel: " + str(e.get_nivel()))
            self.mostrar_estado(e)

    def draw(self, screen):
        rs = pygame.Rect((self.position[1]*SIZE_BLOCK, self.position[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
        pygame.draw.rect(screen, (255, 213, 87), rs)

class Pivot():
    """docstring for pivot."""

    def __init__(self, state):
        self.state = state

    def get_pivot_position(self):
        return self.state.get_position()

    def draw(self, screen):
        r = pygame.Rect((self.state.get_position()[1]*SIZE_BLOCK, self.state.get_position()[0]*SIZE_BLOCK),(SIZE_BLOCK, SIZE_BLOCK))
        pygame.draw.rect(screen, (0, 195, 255), r)

    def move(self, new_state, maze):
        new_state.imprimir()
        maze.set_current_state(new_state)
        self.state = new_state
        print(len(maze.historial))
        maze.historial.append(new_state)
        print(len(maze.historial))
        print(new_state.imprimir())
        aux = self.state.get_position()
        print(f"current pivot state: {self.state.imprimir()}")


class Maze():

    def __init__(self):
        self.current_state = None
        self.spaces = []
        self.queue = []
        self.historial = []
        self.end = None

    def left_pop(self):
        return self.queue.pop(0)

    def get_current_state(self):
        return self.current_state

    def get_spaces(self):
        return self.spaces

    def get_historial(self):
        return self.historial

    def set_current_state(self, state):
        self.current_state = state

    def set_end(self, pos):
        self.end = pos

    def pivot_can_move(self, pivot, move, successor, state):
        temp_state = State((pivot.state.get_position()[0]+move[0], pivot.state.get_position()[1]+move[1]), state)
        if (temp_state.get_position() in self.spaces) and not (temp_state in self.historial):
            successor.append(temp_state)

    def finished(self, pos):
        return self.end == pos

    def depth_first_search(self, successor):
        while len(successor) > 0:
            self.queue.insert(0,successor.pop())

    def breadth_first_search(self, successor):
        while len(successor) > 0:
            self.queue.append(successor.pop(0))

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

    successor = []

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
                maze.set_end((f,c))
            elif maze_map[f][c] == "I":
                state = State((f,c), None)
                pivot = Pivot(state)
                maze.spaces.append((f,c))
                maze.set_current_state(state)
                maze.historial.append(state)
                print(f"start state: {pivot.state.imprimir()}")

    maze.draw(screen, maze_map)
    pivot.draw(screen)
    pygame.display.update()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for move in moves:
            maze.pivot_can_move(pivot, move, successor, maze.get_current_state())

        if len(successor) > 0:
            checkpoint = maze.current_state
        else:
            while not maze.current_state.search_origin(checkpoint):
                pass

        maze.depth_first_search(successor)
        # maze.breadth_first_search(successor)

        if maze.finished(pivot.state.position):
            clock.tick(1)
            print("Finish")
            run = False
            break

        # maze.draw(screen, maze_map)

        pivot.move(maze.left_pop(), maze)
        pivot.draw(screen)
        clock.tick(30)
        pygame.display.update()
