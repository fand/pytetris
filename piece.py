# coding:utf-8

import numpy as np
from random import *
import copy

class Piece():
    
    shape_prototype = {
        0: np.array([[0]]),
        1: np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]]),    #cyan
        2: np.array([[1,1],[1,1]]),    #yellow
        3: np.array([[0,0,0],[1,1,1],[0,1,0]]),    #'violet
        4: np.array([[1,1,0],[0,1,1],[0,0,0]]),    #'red'
        5: np.array([[0,1,1],[1,1,0],[0,0,0]]),    #'green'
        6: np.array([[0,0,0],[1,1,1],[1,0,0]]),    #'orange'
        7: np.array([[0,0,0],[1,1,1],[0,0,1]])    #'blue'
        }


    def __init__(self, board):
        self.type = randint(1,7)
        self.shape = copy.deepcopy(Piece.shape_prototype[self.type])
        self.x = 6 + int(len(self.shape) / (-2))
        self.y = 3 + int(len(self.shape) / (-2))
        self.board = board.getShape()
        for i in range(randint(0,4)):
            self.rotate('cw')
        self.interval = {
            "move": 0.3,
            "rotate": 0.3
            }

    def getShape(self):
        return self.shape

    def getType(self):
        return self.type

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setBoard(self, newboard):
        self.Board = newboard
        
    def isMovable(self,dir):
        for i in range(len(self.shape)):
            for j in range(np.size(self.shape[i])):
                if self.shape[i][j]:
                    if dir == 'left':
                        if self.board[self.y+i][self.x+j-1] != 0: return False 
                    if dir == 'right':
                        if self.board[self.y+i][self.x+j+1] != 0: return False 
                    if dir == 'down':
                        if self.board[self.y+i+1][self.x+j] != 0: return False 
        return True
    
    def move(self,dir):
        if self.isMovable(dir):
            if dir == 'left': self.x -= 1 
            if dir == 'right': self.x += 1 
            if dir == 'down': self.y += 1
            
    def rotate(self,rad):
        if rad == 'ccw':
            tmp = np.rot90(self.shape)
        elif rad == 'cw':
            tmp = np.rot90(self.shape,3)
        x_tmp = copy.copy(self.x)
        y_tmp = copy.copy(self.y)
        # ずらしたら回転できないか試行する
        trial = 0
        while trial < 4:
            cleared = True
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    if tmp[i][j]:
                        if y_tmp+i<0:
                            y_tmp += 1
                            cleared = False
                            continue
                        elif y_tmp+i>21:
                            y_tmp -= 1
                            cleared = False
                            continue
                        elif x_tmp+j<0:
                            if trial == 0:
                                x_tmp += 1
                                trial = 1
                            cleared = False
                            continue
                        elif x_tmp+j>11:
                            if trial==1:
                                x_tmp -= 1
                                trial = 2
                            cleared = False
                            continue
                        elif self.board[y_tmp+i][x_tmp+j]!=0:
                            if trial == 0:
                                x_tmp+=1
                            elif trial == 1:
                                x_tmp-=2
                            elif trial == 2:
                                x_tmp+=1
                                y_tmp-=1
                            elif trial == 3:
                                y_tmp+=1
                            trial += 1
                            cleared = False
            if cleared:
                self.x = x_tmp
                self.y = y_tmp
                self.shape = tmp
                trial = 100

    def drop(self):
        while self.isMovable('down'):
            self.y += 1
        
    def isGround(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j]:
                    if self.board[self.y+i+1][self.x+j]!=0:
                        return True
        return False
                        
