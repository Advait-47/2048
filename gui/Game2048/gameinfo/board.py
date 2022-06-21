import pygame
from .constants import *
import numpy as np
import math

pygame.init()


class Board:
    def __init__(self, WIN):
        file = open("hScore.txt", "r")
        self.highScore = file.read()
        file.close()

    def boardChange(self, arr, WIN, score):
        self.arr = arr
        font = pygame.font.SysFont('arial', FONT_SIZE, bold=True)
        WIN.fill(BORDER_COLOR)

        for i in range(0, ROWS, 1):
            for j in range(0, COLS, 1):
                if(arr[i][j] != 0):
                    pygame.draw.rect(WIN, self.getColor(arr[i][j]), (j*(SQUARE_SIZE)+(
                        j+1)*PADDING, i*(SQUARE_SIZE)+(i+1)*PADDING, SQUARE_SIZE, SQUARE_SIZE))
                    text = font.render(
                        str(self.arr[i][j]), True, WHITE, None)
                else:
                    text = font.render(" ", True, WHITE, None)
                    pygame.draw.rect(WIN, BLANK_COLOR, (j*(SQUARE_SIZE)+(j+1)*PADDING,
                                     i*(SQUARE_SIZE)+(i+1)*PADDING, SQUARE_SIZE, SQUARE_SIZE))

                textRect = text.get_rect()
                textRect.center = (
                    (SQUARE_SIZE*j)+((j+1)*PADDING)+(SQUARE_SIZE//2), (SQUARE_SIZE*i) + ((i+1)*PADDING) + (SQUARE_SIZE//2))
                WIN.blit(text, textRect)

        textData = self.getText(WIN, 'arial', 40, True,
                                "Score:", WHITE, (100, 700))
        WIN.blit(textData[0], textData[1])

        textData = self.getText(WIN, 'arial', 40, True,
                                str(score), WHITE, (220, 700))
        WIN.blit(textData[0], textData[1])

        textData = self.getText(WIN, 'arial', 40, True,
                                "Best:", WHITE, (350, 700))
        WIN.blit(textData[0], textData[1])

        if(score > int(self.highScore)):
            textData = self.getText(
                WIN, 'arial', 40, True, str(score), WHITE, (500, 700))
        else:
            textData = self.getText(
                WIN, 'arial', 40, True, self.highScore, WHITE, (500, 700))

        WIN.blit(textData[0], textData[1])

        pygame.display.update()

    def getColor(self, z):
        z = math.log2(z)
        z = z % 12
        x = z//4

        if(x == 0):
            return (255, 63, ((255//4) * (z % 4))+64)
        if(x == 1):
            return(63, ((255//4) * (z % 4))+64, 255)
        if(x == 2):
            return(((255//4) * (z % 4))+64, 255, 63)

    def gameOver(self, WIN):

        s = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        s.set_alpha(127)
        s.fill((255, 255, 255))
        WIN.blit(s, (0, 0))

        textData = self.getText(
            WIN, 'arial', 40, True, "Game Over", BLACK, (WIN_WIDTH//2, WIN_HEIGHT//2))
        WIN.blit(textData[0], textData[1])

        textData = self.getText(
            WIN, 'arial', 20, True, "Press Esc key to exit", BLACK, (WIN_WIDTH//2, (WIN_HEIGHT//2)+50))
        WIN.blit(textData[0], textData[1])

        pygame.display.update()

    def getText(self, WIN, fontType, fontSize, boldness, text, fontColor, Coords):
        font = pygame.font.SysFont(fontType, fontSize, bold=boldness)
        textRendered = font.render(text, True, fontColor, None)
        textRect = textRendered.get_rect()
        textRect.center = (Coords)
        return [textRendered, textRect]
