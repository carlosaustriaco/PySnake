import GeneralConstants as gc
import pygame
import random

class Apple:
    _pos = (0, 0)

    def __init__(self):
        self._apple_surface = pygame.Surface((gc.PIXEL_SIZE, gc.PIXEL_SIZE))
        self._apple_surface.fill(gc.APPLE_COLOR)

    def UpdatePosition(self):
        x = random.randint(0, gc.BOARD_WIDTH)
        y = random.randint(0, gc.BOARD_HEIGHT)

        x = x // gc.PIXEL_SIZE * gc.PIXEL_SIZE
        y = y // gc.PIXEL_SIZE * gc.PIXEL_SIZE
         
        self._pos = (x, y)

    def GetPosition(self):
        return self._pos