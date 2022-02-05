"""
This file contains the game initialization and main game loop.
"""
import pygame
from static import PARAMS
from interface import Interface
from board import Board

class Game():
    def __init__(self):
        # initialize pygame modules and objects
        pygame.init()
        self.clock = pygame.time.Clock()

        # initialize game components
        self.board = Board()

        # initialize the interface
        self.interface = Interface(self.board)

        # 
        self.running = True

    # actual loop update content
    def __update__(self):
        # exit event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # 30 FPS game loop
    def gameloop(self):
        while self.running:
            self.__update__()
            self.interface.__update__()
            self.clock.tick(30)
