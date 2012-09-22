# coding:utf-8
import pygame
from pygame.locals import *
import copy

from cell import *


class PtView:
    SCREEN_SIZE = (480,480)
    
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode(PtView.SCREEN_SIZE)
        self.sysfont = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.cells = Cell.getCells()
        pygame.display.set_caption(u"TETRIS")

    def renderText(self, text, color, bg_color, x, y):
        self.screen.blit(self.sysfont.render(text, True, color, bg_color), (x, y))
        
    def renderBoard(self, board):
        for i in range(2,len(board)):
            for j in range(len(board[i])):
                x = j * Cell.SIZE
                y = (i-2) * Cell.SIZE
                self.cells[board[i][j]].render(self.screen, x, y)
        
    def renderScore(self, score):
        self.renderText('SCORE:', (200,160,160), (0,0,0), 280, 50)
        self.renderText(str("%08d" % score), (220,220,220),(0,0,0), 310, 100)
    
    def renderNext(self, p_shape, p_type):
        self.renderText('NEXT:', (200,160,160), (0,0,0), 280, 200)

        #erasing old Next
        pygame.draw.rect(self.screen, (0,0,0), Rect(300,250,300,300))
        for i in range(len(p_shape)):
            for j in range(len(p_shape[i])):
                if p_shape[i][j] != 0:
                    offset_x = 360 - len(p_shape)/2 * Cell.SIZE
                    offset_y = 270
                    x = j * Cell.SIZE + offset_x
                    y = i * Cell.SIZE + offset_y
                    self.cells[p_type].render(self.screen, x, y)
                    

                    
