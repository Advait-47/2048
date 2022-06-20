import pygame
from gameinfo.board import *
from gameinfo.constants import *
from gameinfo.gamedriver import *

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('2048')


def main():
    flags = [False, False]
    run = True
    clock = pygame.time.Clock()
    game = driver(WIN)

    game.generateNextCell()
    game.printMat(WIN)
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    flags = moveDriver(game, "a")
                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    flags = moveDriver(game, "d")
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    flags = moveDriver(game, "w")
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    flags = moveDriver(game, "s")

                if(flags[1] and flags[2]):
                    game.gameOver(WIN)
                    run = False
    pygame.quit()


def moveDriver(game, move):
    flags = game.makeAMove(move)
    if(flags[0]):
        game.generateNextCell()
        game.printMat(WIN)
    return flags


main()
