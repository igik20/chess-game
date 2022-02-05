"""
This file contains the interface for handling board squares.
"""
import pygame
from static import PARAMS, COLORS

class Square():
    def __init__(self, x, y, file, row) -> None:
        self.x = x
        self.y = y
        self.color = COLORS.SQDARK if ( (x + y) // 125) % 2 == 1 else COLORS.SQLIGHT
        self.file = file
        self.row = row

    def coord(self):
        return f"{self.file}{self.row}"

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, PARAMS.SQRSIZE, PARAMS.SQRSIZE))
        caption = font.render(self.coord(), True, (0,0,0))
        screen.blit(caption, (self.x + 8, self.y + 8))
