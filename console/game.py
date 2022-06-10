from math import floor
import random
from time import sleep
from tkinter.tix import MAIN
import numpy as np

arr = np.zeros((4, 4), int)
random.seed()


def generateNextCell():
    x = floor((random.random())*16)
    if(arr[x//4][x % 4] == 0):
        y = floor(random.random()*10)
        if(y < 1):
            arr[x//4][x % 4] = 4
        else:
            arr[x//4][x % 4] = 2


def printMat():
    for i in range(4):
        for j in range(4):
            print(arr[i][j], end=" ")
        print("\n")


if __name__ == "__main__":
    generateNextCell()
    printMat()
