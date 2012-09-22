# coding:utf-8
import pygame
from pygame.locals import *
import copy
import time
import numpy as np
from random import *

import model


class PyTetris:
    
    def __init__(self,gravity=0.3):
        pygame.init()
        self.model = model.PtModel(gravity)
        pygame.key.set_repeat(150, 40)

    def alive(self):
        return self.model.isAlive()
    
    def loop(self):
        self.model.loop()
        
    def quit(self):        
        pygame.quit()

        
if __name__ == '__main__':
    pt = PyTetris()
    while pt.alive():
            pt.loop()
    pt.quit()
        
    
