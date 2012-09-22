# coding:utf-8
import pygame
from pygame.locals import *
import copy
import time

import pprint

from piece import Piece
from view import PtView
from board import Board

class PtModel:
    #class variables
    FPS = 60
    SCORE = [0, 40, 100, 300, 1200]
    TIME = {
        "fell": -100,
        "moved": -100,
        "rotated": -20,
        "stopped_moving": -30,
        "stopped_rotating":-30
        }
    INTERVAL = {
        "move": 0.3,
        "rotate": 0.3,
        "gravity": 0.3
        }
    
    def __init__(self, gravity = 0.3):
        self.view =  PtView()
        self.board = Board()
        self.p =  Piece(self.board)
        self.p_next = Piece(self.board)
        self.score = 0
        self.line_erasable = []
        self.interval = copy.deepcopy(PtModel.INTERVAL)
        self.interval['gravity'] = gravity
        self.time = copy.deepcopy(PtModel.TIME)

        self.flag = {
            'moving': True,
            'rotating': True
            }
        
        self.view.renderNext(self.p_next.getShape(), self.p_next.getType())
        
    def getKey(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        # 移動のキーn
        if self.isMovable():
            if keys[K_LEFT]:
                self.movePiece('left')
            elif keys[K_RIGHT]:
                self.movePiece('right')
            elif keys[K_UP]:
                self.movePiece('up')
            elif keys[K_DOWN]:
                self.movePiece('down')
                if self.p.isGround() == False:
                    self.time['moved'] = time.clock()
            else:
                # 動くのをやめた時だけインターバル回復
#                if self.flag['moving']:
                self.flag['moving'] = False
                self.time['stopped_moving'] = time.clock()
                self.interval['move'] = PtModel.INTERVAL['move']

        # 回転のキー
        if self.isRotatable():
            if keys[K_z]:
                self.rotatePiece('ccw')
            elif keys[K_x]:
                self.rotatePiece('cw')
            else:
 #               if self.flag['rotating']:
                self.flag['rotating'] = False
                self.time['stopped_rotating'] = time.clock()
                self.interval['rotate'] = PtModel.INTERVAL['rotate']

    def isMovable(self):
        if (time.clock() - self.time['moved']) > self.interval['move']:
            return True
        if (time.clock() - self.time['stopped_moving'])< PtModel.INTERVAL['move']:
            return True
        return False
    
    def isRotatable(self):
        if (time.clock() - self.time['rotated']) > self.interval['rotate']:
            return True
        if (time.clock() - self.time['stopped_rotating'])< PtModel.INTERVAL['rotate']:
            return True
        return False
    
    def movePiece(self, direction):
        if direction == 'up':
            self.p.drop()
        else:
            self.p.move(direction)
        self.time['moved'] = time.clock()
        if self.interval['move'] > 0.1:
            self.interval['move'] *= 0.9
#        self.flag['moving'] = True

    def rotatePiece(self, radius):
        self.p.rotate(radius)
        self.time['rotated'] = time.clock()
        if(self.interval['rotate']>0.1):
            self.interval['rotate'] *= 0.9
#        self.flag['rotating'] = True

    def fallPiece(self):
        if time.clock() - self.time['fell'] > self.interval['gravity']:
            self.time['fell'] = time.clock()
            self.p.move('down')
            self.time['moved'] = time.clock()
    
    def isAlive(self):
        for i in self.board.getShape()[3]:
            if i!=0 and i!=8: return False
        return True
    
    def updateBoard(self):
        p_shape = self.p.getShape()
        p_type = self.p.getType()
        self.board.update(p_shape, p_type, self.p.getX(), self.p.getY())

    def updatePiece(self):
        self.p = copy.deepcopy(self.p_next)
        self.p.setBoard(self.board)
        self.p_next = Piece(self.board)
        self.view.renderNext(self.p_next.getShape(), self.p_next.getType())

    def update(self):
        if self.isWaiting():
            return False
        self.updateBoard()
        self.erase()
        self.updatePiece()
        return True
            
    def erase(self):
        self.score += PtModel.SCORE[self.board.erase()]

    def isWaiting(self):
        if self.p.isGround():
            if time.clock() - self.time['moved'] < self.interval['gravity']:
                return True
            if time.clock() - self.time['rotated'] < self.interval['gravity']:
                return True
            return False
        return True
    
    def gameOver(self):
        pass
    
    def tick(self):
        pygame.time.Clock().tick(15)

    # boardとpieceを統合して現在の画面の状態を得る
    def getCurrentBoard(self):
        b_shape = copy.deepcopy(self.board.getShape())
        p_shape = self.p.getShape()
        p_type = self.p.getType()
        offset_x = self.p.getX()
        offset_y = self.p.getY()
        for i in range(len(p_shape)):
            for j in range(len(p_shape[i])):
                if p_shape[i][j]:
                    b_shape[i + offset_y][j + offset_x] = p_type
        return b_shape

    def draw(self):
        self.view.renderBoard(self.getCurrentBoard())
        self.view.renderScore(self.score)
        pygame.display.update()
    
    def loop(self):
        self.tick()
        self.update()
        if self.isAlive() == False:
            self.gameOver()
        self.getKey()
        self.fallPiece()
        self.draw()
