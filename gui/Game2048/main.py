import pygame
from gameinfo.board import *
from gameinfo.constants import *
from gameinfo.gamedriver import *

pygame.init()
FPS = 60

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('2048')


def main():
    randOrNot = False
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
                over = game.allFilled()
                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    randOrNot = game.makeAMove("a")
                    twoLineCode(game, randOrNot)
                    randOrNot = False
                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    randOrNot = game.makeAMove("d")
                    twoLineCode(game, randOrNot)
                    randOrNot = False
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    randOrNot = game.makeAMove("w")
                    twoLineCode(game, randOrNot)
                    randOrNot = False
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    randOrNot = game.makeAMove("s")
                    twoLineCode(game, randOrNot)
                    randOrNot = False
    pygame.quit()


def twoLineCode(game, randOrNot):
    if(randOrNot):
        game.generateNextCell()
        game.printMat(WIN)
    else:
        game.gameOver(WIN)


main()
