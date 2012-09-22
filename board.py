#coding:utf-8

import pygame
import copy

class Board:
    SHAPE =    [[8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,0,8],
                [8,8,8,8,8,8,8,8,8,8,8,8]]

    def __init__(self, shape=None):
        if shape != None:
            self.shape = shape
        else:
            self.shape = copy.deepcopy(Board.SHAPE)
        self.line_erasable = []

    def update(self, p_shape, p_type, x, y):
        for i in range(len(p_shape)):
            for j in range(len(p_shape[i])):
                if p_shape[i][j]:
                    self.shape[y + i][x + j] = p_type
    
    def getShape(self):                       
        return self.shape

    # 上から順番にline_erasableに入る
    def checkErase(self):
        for i in range(len(self.shape[:-1])):
            if len([x for x in self.shape[i] if x==0]) == 0:
                self.line_erasable.append(i)
    
    def isErasable(self):
        self.checkErase()
        return len(self.line_erasable)
    
    def erase(self):    # 消した列の数を返す
        if self.isErasable() == False:
            return 0
        count_erased = len(self.line_erasable)
        for i in self.line_erasable:
            for j in range(i):
                self.shape[i-j] = copy.deepcopy(self.shape[i-j-1])
        self.line_erasable = []
        return count_erased

