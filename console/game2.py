from math import floor
import random
from time import sleep
import numpy as np
# from pip import main

x = int(4)
y = int(4)

arr = np.zeros((x, y), int)
random.seed()


def generateNextCell():
    while(1):
        rnum = floor((random.random())*(x*y))
        if(arr[rnum//x][rnum % y] == 0):
            genNewNumProb = floor(random.random()*10)
            if(genNewNumProb < 1):
                arr[rnum//x][rnum % y] = 4
            else:
                arr[rnum//x][rnum % y] = 2
            break


def makeAMove():
    move = input()
    swipeTile(move)
    printMat()
    mergeTile(move)
    printMat()
    swipeTile(move)
    printMat()


def swipeTile(move):
    if(move == 'w'):
        for i in range(1, x, 1):
            for j in range(i, 0, -1):
                for k in range(0, y, 1):
                    # if(arr[j][k] == arr[j-1][k]):
                    #     arr[j-1][k] *= 2
                    #     arr[j][k] = 0
                    if(arr[j-1][k] == 0):
                        arr[j-1][k] = arr[j][k]
                        arr[j][k] = 0
    if(move == 'a'):
        for i in range(1, y, 1):
            for j in range(i, 0, -1):
                for k in range(0, x, 1):
                    # if(arr[k][j] == arr[k][j-1]):
                    #     arr[k][j-1] *= 2
                    #     arr[k][j] = 0
                    if(arr[k][j-1] == 0):
                        arr[k][j-1] = arr[k][j]
                        arr[k][j] = 0
    if(move == 's'):
        for i in range(x-2, -1, -1):
            for j in range(i, x-1, 1):
                for k in range(0, y, 1):
                    # if(arr[j][k] == arr[j+1][k]):
                    #     arr[j+1][k] *= 2
                    #     arr[j][k] = 0
                    if(arr[j+1][k] == 0):
                        arr[j+1][k] = arr[j][k]
                        arr[j][k] = 0
    if(move == 'd'):
        for i in range(y-2, -1, -1):
            for j in range(i, y-1, 1):
                for k in range(0, x, 1):
                    # if(arr[k][j] == arr[k][j+1]):
                    #     arr[k][j+1] *= 2
                    #     arr[k][j] = 0
                    if(arr[k][j+1] == 0):
                        arr[k][j+1] = arr[k][j]
                        arr[k][j] = 0


def mergeTile(move):
    if(move == 'w'):
        for i in range(1, x, 1):
            for j in range(0, y, 1):
                if(arr[i-1][j] == arr[i][j]):
                    arr[i-1][j] *= 2
                    arr[i][j] = 0
    if(move == 'a'):
        for i in range(1, y, 1):
            for j in range(0, x, 1):
                if(arr[j][i-1] == arr[j][i]):
                    arr[j][i-1] *= 2
                    arr[j][i] = 0
    if(move == 's'):
        for i in range(x-2, -1, -1):
            for j in range(0, y, 1):
                if(arr[i+1][j] == arr[i][j]):
                    arr[i+1][j] *= 2
                    arr[i][j] = 0
    if(move == 'd'):
        for i in range(y-2, -1, -1):
            for j in range(0, x, 1):
                if(arr[j][i+1] == arr[j][i]):
                    arr[j][i+1] *= 2
                    arr[j][i] = 0


def printMat():
    print("")
    cellString = "{: <5} "
    rowString = y*cellString
    for row in arr:
        print(rowString.format(*row))
        # for j in range(4):
        #     print(arr[i][j], end=" ")
        # print("\n")
    print("")


def allFilled():
    flag = True
    for i in range(0, x, 1):
        for j in range(0, y, 1):
            if(arr[i][j] == 0):
                flag = False
    return flag


if __name__ == "__main__":
    generateNextCell()
    printMat()
    while(not(allFilled())):
        print("START")
        makeAMove()
        print("END")
        generateNextCell()
        printMat()
    printMat()
    print("Game Over!")
