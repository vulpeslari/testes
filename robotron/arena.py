import pygame


class Arena:
    def __init__(self, screen, sc_width, sc_height):
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.screen = screen
        self.red = 255
        self.blue = 1
        self.aux = 4

    def run(self):
        pygame.draw.rect(self.screen, (255, 123, 1), (110, 110, 40, 40))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 10, 620))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (1200, 100, 10, 620))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 100, 1100, 10))
        pygame.draw.rect(self.screen, (self.red, 0, self.blue), (100, 710, 1100, 10))

        self.blue += self.aux
        self.red -= self.aux

        if self.blue >= 255 or self.blue <= 0:
            self.blue = 1
        if self.red <= 0 or self.red >= 255:
            self.red = 255

