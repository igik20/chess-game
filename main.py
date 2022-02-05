"""
Program entry point for Chess Game.
"""
import pygame
from square import Square
from static import PARAMS
from game import Game

# initialize
game = Game()
quitclock = pygame.time.Clock()

# start and maintain game loop
game.gameloop()

pygame.quit()
