"""
This file contains the game initialization and main game loop.
"""
from sqlalchemy import null
import pygame
from static import PARAMS, COLORS
from interface import Interface
from board import Board
from piece import Piece

class Game():
    def __init__(self):
        # initialize pygame modules and objects
        pygame.init()
        self.clock = pygame.time.Clock()

        # initialize game components
        self.board = Board()
        self.pieces = [Piece(self.board)]
        self.moved_piece = null

        # initialize the interface
        self.interface = Interface(self.board, self.pieces)

        # start the game
        self.running = True

    # actual loop update content
    def __update__(self):
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # self.board.reset_colors()
                x, y = pygame.mouse.get_pos()
                # self.board.get_square(x, y).color = COLORS.LIGHTGREEN
                for piece in self.pieces:
                    if piece.is_clicked(x,y):
                        self.moved_piece = piece
                        self.moved_piece.r = 60
            elif event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                s = self.board.get_square(mx, my)
                self.moved_piece.x = s.x
                self.moved_piece.y = s.y
                self.moved_piece.r = 50
                self.moved_piece = null
        if self.moved_piece is not null:
            x, y = pygame.mouse.get_pos()
            self.moved_piece.x = x - PARAMS.SQRSIZE / 2
            self.moved_piece.y = y - PARAMS.SQRSIZE / 2

    # 30 FPS game loop
    def gameloop(self):
        while self.running:
            self.__update__()
            self.interface.__update__()
            self.clock.tick(30)
