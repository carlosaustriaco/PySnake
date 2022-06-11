import pygame
from pygame.locals import *
import random
import GeneralConstants as gc
from Board import Board

def collision(pos1, pos2):
    return pos1 == pos2

def OffLimits(pos):
    return not ((0 <= pos[0] < gc.BOARD_WIDTH) and (0 <= pos[1] < gc.BOARD_HEIGHT))

def StartGame():
    board = Board()

pygame.init()
screen = pygame.display.set_mode(gc.WINDOW_SIZE)
pygame.display.set_caption("Snake")

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((gc.PIXEL_SIZE, gc.PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

apple_surface = pygame.Surface((gc.PIXEL_SIZE, gc.PIXEL_SIZE))
apple_surface.fill((255, 0, 0))

def RandomOnGrid():
    x = random.randint(0, gc.BOARD_WIDTH)
    y = random.randint(0, gc.BOARD_HEIGHT)

    return x // gc.PIXEL_SIZE * gc.PIXEL_SIZE, y // gc.PIXEL_SIZE * gc.PIXEL_SIZE

apple_pos = RandomOnGrid()

while(True):
    pygame.time.Clock().tick(15)
    screen.fill((0, 0 ,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    if collision(snake_pos[0], apple_pos):
        snake_pos.append((-10, -10))
        apple_pos = RandomOnGrid()
    
    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            pygame.quit()
            quit()
        snake_pos[i] = snake_pos[i - 1]

    if OffLimits(snake_pos[0]):
        pygame.quit()
        quit()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - gc.PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - 10, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + 10, snake_pos[0][1])
    if snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + gc.PIXEL_SIZE)

    pygame.display.update()