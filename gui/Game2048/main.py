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
                    flags = game.makeAMove("a")
                    print(flags)
                    twoLineCode(game, flags)
                if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    flags = game.makeAMove("d")
                    twoLineCode(game, flags)
                if(event.key == pygame.K_UP or event.key == pygame.K_w):
                    flags = game.makeAMove("w")
                    twoLineCode(game, flags)
                if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    flags = game.makeAMove("s")
                    twoLineCode(game, flags)

                if(flags[1] and flags[2]):
                    print("It's Over\n")
                    game.gameOver(WIN)
                    run = False

    pygame.quit()


def twoLineCode(game, flags):
    if(flags[0]):
        game.generateNextCell()
        game.printMat(WIN)


main()
