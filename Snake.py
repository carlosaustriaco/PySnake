import pygame
import GeneralConstants as gc
from pygame.locals import *

class Snake:
    _pos = [(250, 50), (260, 50), (270, 50)]

    def __init__(self):
        self._snake_surface = pygame.Surface((gc.PIXEL_SIZE, gc.PIXEL_SIZE))
        self._snake_surface.fill(gc.SNAKE_COLOR)
        self._direction = K_LEFT

    def MoveSnake(self):
        for i in range(len(self._pos) - 1, 0, -1):
            self._pos[i] = self._pos[i - 1]

        #Updating the head position
        if self._direction == K_UP:
            self._pos[0] = (self._pos[0][0], self._pos[0][1] - gc.PIXEL_SIZE)
        elif self._direction == K_DOWN:
            self._pos[0] = (self._pos[0][0], self._pos[0][1] + gc.PIXEL_SIZE)
        elif self._direction == K_LEFT:
            self._pos[0] = (self._pos[0][0] - gc.PIXEL_SIZE, self._pos[0][1])
        elif self._direction == K_RIGHT:
            self._pos[0] = (self._pos[0][0] + gc.PIXEL_SIZE, self._pos[0][1])

    def GrowSnake(self):
        self._pos.append((-10, -10))
        self.MoveSnake()

    def GetHeadPos(self):
        return self._pos[0]

    def UpdateSnakeDirection(self, a_event):
        if a_event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                self._direction = a_event.key