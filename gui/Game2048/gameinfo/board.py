import pygame
from .constants import *
import numpy as np
import math

pygame.init()


class Board:
    def __init__(self, WIN):
        pass

    def boardChange(self, arr, WIN, score):
        self.arr = arr
        font = pygame.font.SysFont('arial', FONT_SIZE, bold=True)
        WIN.fill(BORDER_COLOR)
        # WIN.fill(BORDER_COLOR)
        # WIN.blit(text, textRect)

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

        text = font.render("Score:", True, WHITE, None)
        textRect = text.get_rect()
        textRect.center = (100, 700)  # HEIGHT+((WIN_HEIGHT-HEIGHT)//2)
        WIN.blit(text, textRect)

        text = font.render(str(score), True, WHITE, None)
        textRect = text.get_rect()
        textRect.center = (250, 700)  # HEIGHT+((WIN_HEIGHT-HEIGHT)//2)
        WIN.blit(text, textRect)
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
        pass
