from math import floor
import random
from time import sleep
import numpy as np
from .board import *

pygame.init()
x = int(4)
y = int(4)

random.seed()


class driver:
    def __init__(self):
        self.arr = np.zeros((x, y), int)
        self.palette = Board()

    def generateNextCell(self):
        while(1):
            rnum = floor((random.random())*(x*y))
            if(self.arr[rnum//x][rnum % y] == 0):
                genNewNumProb = floor(random.random()*10)
                if(genNewNumProb < 1):
                    self.arr[rnum//x][rnum % y] = 4
                else:
                    self.arr[rnum//x][rnum % y] = 2
                break

    def makeAMove(self, move):
        #move = input()
        self.swipeTile(move)
        # printMat()
        self.mergeTile(move)
        # printMat()
        self.swipeTile(move)
        # printMat()

    def swipeTile(self, move):
        if(move == 'w'):
            for i in range(1, x, 1):
                for j in range(i, 0, -1):
                    for k in range(0, y, 1):
                        # if(self.arr[j][k] == self.arr[j-1][k]):
                        #     self.arr[j-1][k] *= 2
                        #     self.arr[j][k] = 0
                        if(self.arr[j-1][k] == 0):
                            self.arr[j-1][k] = self.arr[j][k]
                            self.arr[j][k] = 0
        if(move == 'a'):
            for i in range(1, y, 1):
                for j in range(i, 0, -1):
                    for k in range(0, x, 1):
                        # if(self.arr[k][j] == self.arr[k][j-1]):
                        #     self.arr[k][j-1] *= 2
                        #     self.arr[k][j] = 0
                        if(self.arr[k][j-1] == 0):
                            self.arr[k][j-1] = self.arr[k][j]
                            self.arr[k][j] = 0
        if(move == 's'):
            for i in range(x-2, -1, -1):
                for j in range(i, x-1, 1):
                    for k in range(0, y, 1):
                        # if(self.arr[j][k] == self.arr[j+1][k]):
                        #     self.arr[j+1][k] *= 2
                        #     self.arr[j][k] = 0
                        if(self.arr[j+1][k] == 0):
                            self.arr[j+1][k] = self.arr[j][k]
                            self.arr[j][k] = 0
        if(move == 'd'):
            for i in range(y-2, -1, -1):
                for j in range(i, y-1, 1):
                    for k in range(0, x, 1):
                        # if(self.arr[k][j] == self.arr[k][j+1]):
                        #     self.arr[k][j+1] *= 2
                        #     self.arr[k][j] = 0
                        if(self.arr[k][j+1] == 0):
                            self.arr[k][j+1] = self.arr[k][j]
                            self.arr[k][j] = 0

    def mergeTile(self, move):
        if(move == 'w'):
            for i in range(1, x, 1):
                for j in range(0, y, 1):
                    if(self.arr[i-1][j] == self.arr[i][j]):
                        self.arr[i-1][j] *= 2
                        self.arr[i][j] = 0
        if(move == 'a'):
            for i in range(1, y, 1):
                for j in range(0, x, 1):
                    if(self.arr[j][i-1] == self.arr[j][i]):
                        self.arr[j][i-1] *= 2
                        self.arr[j][i] = 0
        if(move == 's'):
            for i in range(x-2, -1, -1):
                for j in range(0, y, 1):
                    if(self.arr[i+1][j] == self.arr[i][j]):
                        self.arr[i+1][j] *= 2
                        self.arr[i][j] = 0
        if(move == 'd'):
            for i in range(y-2, -1, -1):
                for j in range(0, x, 1):
                    if(self.arr[j][i+1] == self.arr[j][i]):
                        self.arr[j][i+1] *= 2
                        self.arr[j][i] = 0

    def printMat(self, WIN):
        self.palette.boardChange(self.arr, WIN)

        print("")
        cellString = "{: <5} "
        rowString = y*cellString
        for row in self.arr:
            print(rowString.format(*row))
            # for j in range(4):
            #     print(self.arr[i][j], end=" ")
            # print("\n")
        print("")

    def allFilled(self):
        flag = True
        for i in range(0, x, 1):
            for j in range(0, y, 1):
                if(self.arr[i][j] == 0):
                    flag = False
        return flag


# if __name__ == "__main__":
#     generateNextCell()
#     printMat()
#     while(not(allFilled())):
#         # print("START")
#         makeAMove()
#         # print("END")
#         generateNextCell()
#         printMat()
#     # printMat()
#     print("Game Over!")
