import pygame
import GeneralConstants as gc

"""
The class the represents the board of the game
Creation: 11/06/2022 carlosaustriaco
"""
class Board:
    _name = 'Snake'

    def _PaintPosition(self, a_Surface, a_Pos):
        self._screen.blit(a_Surface, a_Pos)

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(gc.WINDOW_SIZE)
        pygame.display.set_caption(self._name)

    def ResetBoard(self):
        self._screen.fill(gc.BOARD_COLOR)    
    
    def PaintApple(self, a_AppleSurface, a_ApplePosition):
        self._PaintPosition(a_AppleSurface, a_ApplePosition)

    def PaintSnake(self, a_SnakeSurface, a_lstSnakePosition):
        for pos in a_lstSnakePosition:
            self._PaintPosition(a_SnakeSurface, pos)
    
    def UpdatePainting(self):
        pygame.display.update()