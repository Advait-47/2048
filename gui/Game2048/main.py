import pygame
from gameinfo.board import *
from gameinfo.constants import *
from gameinfo.gamedriver import *

pygame.init()
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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

                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    if(not(game.allFilled())):
                        randOrNot = game.makeAMove("a")
                        twoLineCode(game, randOrNot)
                        randOrNot = False
                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    if(not(game.allFilled())):
                        randOrNot = game.makeAMove("d")
                        twoLineCode(game, randOrNot)
                        randOrNot = False
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    if(not(game.allFilled())):
                        randOrNot = game.makeAMove("w")
                        twoLineCode(game, randOrNot)
                        randOrNot = False
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    if(not(game.allFilled())):
                        randOrNot = game.makeAMove("s")
                        twoLineCode(game, randOrNot)
                        randOrNot = False
    pygame.quit()


def twoLineCode(game, randOrNot):
    if(randOrNot):
        game.generateNextCell()
        game.printMat(WIN)


main()
