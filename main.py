import time
import random as r
import pygame
from constants import WIDTH, HEIGHT, RED, WHITE, SQUARE_SIZE
from game import Game
from algorithm import Algorithm



FPS = 60
DEPTH = 5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')

def get_col_from_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    return col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        # uncomment this if statement if you want to test your scoring algorithm without an AI.
        if game.turn == WHITE:
          value, new_board = Algorithm.minimax(game.get_board(), DEPTH, True)
          game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = get_col_from_mouse(pos)
                game.add_piece(col)

        game.update()


    pygame.quit()


main()