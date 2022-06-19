import pygame
from gameinfo.board import *
from gameinfo.constants import *
from gameinfo.gamedriver import *

pygame.init()
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    game = driver()

    while(run):
        clock.tick(FPS)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    game.makeAMove("a")
                    game.generateNextCell()
                    game.printMat(WIN)

                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    game.makeAMove("d")
                    game.generateNextCell()
                    game.printMat(WIN)
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    game.makeAMove("w")
                    game.generateNextCell()
                    game.printMat(WIN)
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    game.makeAMove("s")
                    game.generateNextCell()
                    game.printMat(WIN)

    pygame.quit()


main()
