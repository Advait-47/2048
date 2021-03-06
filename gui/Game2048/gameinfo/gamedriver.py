from math import floor
import random
from time import sleep
import numpy as np
from .board import *

pygame.init()
x = int(ROWS)
y = int(COLS)

random.seed()


class driver:
    score = 0
    highScore = 0

    def __init__(self, WIN):
        try:
            file = open("hScore.txt", "r")
            self.highScore = int(file.read())
            file.close()
        except:
            try:
                file = open("hScore.txt", "x")
                file.write("0")
                file.close()
            except:
                pass
            pass

        self.arr = np.zeros((x, y), int)
        self.palette = Board(WIN)

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
        arr2 = self.arr
        r1 = self.swipeTile(move)
        r2 = self.mergeTile(move)
        r3 = self.swipeTile(move)
        return [r1 or r2 or r3, np.array_equal(arr2, self.arr) and self.allFilled(), self.adjCheck()]

    def swipeTile(self, move):
        randOrNot = None

        if(move == 'w'):
            for i in range(1, x, 1):
                for j in range(i, 0, -1):
                    for k in range(0, y, 1):
                        if(self.arr[j-1][k] == 0 and self.arr[j][k] != 0):
                            self.arr[j-1][k] = self.arr[j][k]
                            self.arr[j][k] = 0
                            randOrNot = True

        if(move == 'a'):
            for i in range(1, y, 1):
                for j in range(i, 0, -1):
                    for k in range(0, x, 1):
                        if(self.arr[k][j-1] == 0 and self.arr[k][j] != 0):
                            self.arr[k][j-1] = self.arr[k][j]
                            self.arr[k][j] = 0
                            randOrNot = True

        if(move == 's'):
            for i in range(x-2, -1, -1):
                for j in range(i, x-1, 1):
                    for k in range(0, y, 1):
                        if(self.arr[j+1][k] == 0 and self.arr[j][k] != 0):
                            self.arr[j+1][k] = self.arr[j][k]
                            self.arr[j][k] = 0
                            randOrNot = True

        if(move == 'd'):
            for i in range(y-2, -1, -1):
                for j in range(i, y-1, 1):
                    for k in range(0, x, 1):
                        if(self.arr[k][j+1] == 0 and self.arr[k][j] != 0):
                            self.arr[k][j+1] = self.arr[k][j]
                            self.arr[k][j] = 0
                            randOrNot = True

        return randOrNot

    def mergeTile(self, move):
        randOrNot = None

        if(move == 'w'):
            for i in range(1, x, 1):
                for j in range(0, y, 1):
                    if(self.arr[i-1][j] == self.arr[i][j] and self.arr[i][j] != 0):
                        self.arr[i-1][j] *= 2
                        self.score += self.arr[i-1][j]
                        self.arr[i][j] = 0
                        randOrNot = True

        if(move == 'a'):
            for i in range(1, y, 1):
                for j in range(0, x, 1):
                    if(self.arr[j][i-1] == self.arr[j][i] and self.arr[j][i] != 0):
                        self.arr[j][i-1] *= 2
                        self.score += self.arr[j][i-1]
                        self.arr[j][i] = 0
                        randOrNot = True

        if(move == 's'):
            for i in range(x-2, -1, -1):
                for j in range(0, y, 1):
                    if(self.arr[i+1][j] == self.arr[i][j] and self.arr[i][j] != 0):
                        self.arr[i+1][j] *= 2
                        self.score += self.arr[i+1][j]
                        self.arr[i][j] = 0
                        randOrNot = True

        if(move == 'd'):
            for i in range(y-2, -1, -1):
                for j in range(0, x, 1):
                    if(self.arr[j][i+1] == self.arr[j][i] and self.arr[j][i] != 0):
                        self.arr[j][i+1] *= 2
                        self.score += self.arr[j][i+1]
                        self.arr[j][i] = 0
                        randOrNot = True

        if(self.score > self.highScore):
            try:
                file = open("hScore.txt", "w")
                file.write(str(self.score))
                file.close()
            except:
                file = open("hScore.txt", "x")
                file.write("0")
                file.close()

        return randOrNot

    def printMat(self, WIN):
        self.palette.boardChange(self.arr, WIN, self.score)

        # print("")
        # cellString = "{: <5} "
        # rowString = y*cellString
        # for row in self.arr:
        #     print(rowString.format(*row))
        # print("")

    def allFilled(self):
        flag = True
        for i in range(0, x, 1):
            for j in range(0, y, 1):
                if(self.arr[i][j] == 0):
                    flag = False

        return flag

    def adjCheck(self):
        for i in range(1, x, 1):
            for j in range(0, y, 1):
                if(self.arr[i][j] != 0):
                    if(self.arr[i][j] == self.arr[i-1][j]):
                        return False
                else:
                    return False

        for i in range(0, x, 1):
            for j in range(1, y, 1):
                if(self.arr[i][j] != 0):
                    if(self.arr[i][j] == self.arr[i][j-1]):
                        return False
                else:
                    return False

        return True

    def gameOver(self, WIN):
        self.palette.gameOver(WIN)

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
