import pygame
from arena import Arena
pygame.init()
pygame.font.init()
sc_width = 1300
sc_height = 800
screen = pygame.display.set_mode((sc_width, sc_height))
velocity = 5
speed = 2
arena = Arena(screen, sc_width, sc_height)
