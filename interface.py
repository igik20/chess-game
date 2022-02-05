"""
Interface and rendering functions.
"""
import pygame
from static import PARAMS, COLORS

class Interface():
    def __init__(self, board):
        self.screen = pygame.display.set_mode( (PARAMS.SCRSIZE, PARAMS.SCRSIZE) )
        self.font = pygame.font.SysFont(None, 24)
        
        self.board = board

    def __update__(self):
        self.board.draw(self.screen, self.font)
        pygame.display.flip()