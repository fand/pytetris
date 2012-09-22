# coding:utf-8
import pygame
from pygame.locals import *
import copy

class Cell:
    SIZE = 23
    
    COLOR = [[  0,  0,  0],    # blacd
             [  0,255,255],    # cyan
             [255,255,  0],    # yellow
             [255,  0,255],    # violet
             [255,  0,  0],    # red
             [  0,255,  0],    # green
             [255, 96,  0],    # orange
             [  0,  0,255],    # blue
             [128,128,128],    # gray
             [255,255,255]]    # white
    
    COLOR_LIGHT = [[  0,  0,  0],    # blacd
                   [128,255,255],    # cyan
                   [255,255,128],    # yellow
                   [255,128,255],    # violet
                   [255,128,128],    # red
                   [128,255,128],    # green
                   [255,192, 64],    # orange
                   [128,128,255],    # blue
                   [192,192,192],    # gray
                   [255,255,255]]    # white
    
    COLOR_SHADOW = [[  0,  0,  0],    # blacd
                    [  0,128,128],    # cyan
                    [128,128,  0],    # yellow
                    [128,  0,128],    # violet
                    [128,  0,  0],    # red
                    [  0,128,  0],    # green
                    [128, 32,  0],    # orange
                    [  0,  0,128],    # blue
                    [ 64, 64, 64],    # gray
                    [128,128,128]]    # white
    

    def __init__(self, color=0):
        # 基本色、影、ハイライト用のサーフェスを返す
        self.base = pygame.Surface([Cell.SIZE-4,Cell.SIZE-4])
        self.base.fill(Cell.COLOR[color])
        self.light = pygame.Surface([Cell.SIZE-2,Cell.SIZE-2])
        self.light.fill(Cell.COLOR_LIGHT[color])
        self.shadow = pygame.Surface([Cell.SIZE-1,Cell.SIZE-1])
        self.shadow.fill(Cell.COLOR_SHADOW[color])

    def render(self, screen, x, y):
        screen.blit(self.shadow, [x+1, y+1])
        screen.blit(self.light, [x+1, y+1])
        screen.blit(self.base, [x+3, y+3])

        
    @classmethod
    def getCells(cls):
        return [cls(i) for i in range(len(cls.COLOR))]
    

