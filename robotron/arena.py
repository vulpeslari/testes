import pygame


class Arena:
    def __init__(self, screen, sc_width, sc_height):
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.screen = screen
        self.red = 255
        self.blue = 1
        self.aux = 1

    def run(self):
        pygame.draw.rect(self.screen, (255, 123, self.blue), (110, 110, 40, 40))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 10, 620))
        pygame.draw.rect(self.screen, (self.red, 0 , self.blue), (1200, 100, 10, 620))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 1100, 10))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 720, 1100, 10))
        if self.blue >= 150 or self.blue <= 0:
            self.aux *= -1
        self.blue += self.aux
