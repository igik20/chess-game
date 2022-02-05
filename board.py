"""
Class for keeping board state.
"""
from static import PARAMS
from square import Square

class Board():
    def __init__(self):
        self.grid = []
        for y in range(0, PARAMS.SCRSIZE, PARAMS.SQRSIZE):
            for x in range(0, PARAMS.SCRSIZE, PARAMS.SQRSIZE):
                file = chr(x // PARAMS.SQRSIZE + 97)
                row = chr(- y // PARAMS.SQRSIZE + 56)
                self.grid.append(Square(x, y, file, row))

    def draw(self, screen, font):
        for sqr in self.grid:
            sqr.draw(screen, font)
