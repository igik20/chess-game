import pygame
from static import PARAMS, COLORS

class Piece():
    def __init__(self, board) -> None:
        self.x = 0
        self.y = 0
        self.r = 50

    def draw(self, screen):
        pygame.draw.circle(screen, COLORS.BLACK, (self.x + PARAMS.SQRSIZE / 2, self.y + PARAMS.SQRSIZE / 2), self.r)

    def is_clicked(self, x, y):
        return self.x < x < self.x + PARAMS.SQRSIZE and self.y < y < self.y + PARAMS.SQRSIZE