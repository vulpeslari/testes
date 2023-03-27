import pygame
from sprites import *


class Arena:
    def __init__(self, screen, sc_width, sc_height):
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.screen = screen
        self.red = 255
        self.blue = 1
        self.aux = 4

    def run(self):
        rect_list = []
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 10, 610))
        rect_list.append(pygame.Rect(100, 100, 10, 610))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (1190, 100, 10, 610))
        rect_list.append(pygame.Rect(1190, 100, 10, 610))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 1090, 10))
        rect_list.append(pygame.Rect(100, 100, 1090, 10))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 710, 1100, 10))
        rect_list.append(pygame.Rect(100, 710, 1100, 10))

        self.blue += self.aux
        self.red -= self.aux

        if self.blue >= 255 or self.blue <= 0:
            self.blue = 1
        if self.red <= 0 or self.red >= 255:
            self.red = 255
        return rect_list


