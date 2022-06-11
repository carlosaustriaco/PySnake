import pygame
from pygame.locals import *
import random
import GeneralConstants as gc
from Board import Board
from Apple import Apple
from Snake import Snake

def IsCollision(pos1, pos2):
    return pos1 == pos2

def IsOffLimits(pos):
    return not ((0 <= pos[0] < gc.BOARD_WIDTH) and (0 <= pos[1] < gc.BOARD_HEIGHT))

def ResetGame():
    pygame.quit()
    quit()

def StartGame():
    board = Board()
    apple = Apple()
    snake = Snake()

    while True:
        pygame.time.Clock().tick(gc.TIME_DELAY)
        board.ResetBoard()

        for event in pygame.event.get():
            if event.type == QUIT:
                ResetGame()
            elif event.type == KEYDOWN:
                snake.UpdateSnakeDirection(event)

        board.PaintApple(apple.GetSurface(), apple.GetPosition())
        board.PaintSnake(snake.GetSurface(), snake.GetAllPositions())

        if IsCollision(apple.GetPosition(), snake.GetHeadPos()):
            snake.GrowSnake()
            apple.UpdatePosition()
        else:
            snake.MoveSnake()

            if snake.IsSnakeDead() or IsOffLimits(snake.GetHeadPos()):
                ResetGame()

        board.UpdatePainting()