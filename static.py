"""
This file stores constants used by other classes.
"""
import pygame

# game parameters
class PARAMS():
    SCRSIZE = 1000
    SQRSIZE = SCRSIZE // 8

# color definitions for nicer code
class COLORS():
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    SQLIGHT = pygame.Color(217, 174, 121)
    SQDARK = pygame.Color(110, 76, 35)

# lengthy default values
class DEFAULTS():
    STARTPOS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"