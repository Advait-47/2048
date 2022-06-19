import pygame
from .constants import *
import numpy as np

pygame.init()


class Board:
    def __init__(self):
        pass

    def boardChange(self, arr, WIN):
        self.arr = arr
        font = pygame.font.SysFont('arial', FONT_SIZE)
        for i in range(0, ROWS, 1):
            for j in range(0, COLS, 1):
                text = font.render(
                    str(self.arr[i][j]), True, WHITE, (255, 0, 0))
                WIN.blit(text,
                         ((SQUARE_SIZE*j)+50, (SQUARE_SIZE*i)+50))
                pygame.display.update()

# +(SQUARE_SIZE//2)
# + (SQUARE_SIZE//2)
