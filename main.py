import pygame

pygame.init()

FPS = 69
TILE_SIZE = 20
BLACK = (0,0,0)
GREY = (128,128,128)
YELLOW = (255,255,0)
WIDTH, HEIGHT = (800,800)
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
