import pygame
from board import Board
from player import Player
# from search import Search


#Game settings
WIDTH, HEIGHT = 500, 500
GRID_SIZE = WIDTH/3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60
pygame.init()


def reset(b, p1, p2):

    b.__init__(GRID_SIZE)
    p1.__init__("X", False)
    p2.__init__("O", True)


if __name__ == '__main__':

    TURN = 1
    MAX_TURNS = 9
    pause = False

    board = Board(GRID_SIZE)
    player1 = Player("X", False)
    player2 = Player("O", True)

    while run:

        pos_matrix = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    board.__init__(GRID_SIZE)
                    player1.__init__("X", False)
                    player2.__init__("O", True)
                    TURN = 1
                    pause = False
                    continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    pos_matrix = (int(pos[1]/GRID_SIZE), int(pos[0]/GRID_SIZE))

        #Logic section
        if not pause:
            if TURN%2 == 1:
                if player1.turn(board, pos_matrix, player2):
                    TURN += 1
            else:
                if player2.turn(board, pos_matrix, player1):
                    TURN += 1

            if board.game_over():
                if TURN%2 == 0:
                    print(f"{player1.letter} GANA!")
                else:
                    print(f"{player2.letter} GANA!")
                pause = True
            elif TURN > MAX_TURNS:
                print("EMPATAO")
                pause = True

        #Draw section
        screen.fill(WHITE)
        board.draw(screen)

        clock.tick(FPS)

        pygame.display.update()
