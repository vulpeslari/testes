import math
from config import *


class Bullet:
    def __init__(self, xp, yp, angle):
        self.count = 0
        self.angle = angle
        self.rect = None
        self.xp = 25 + xp + 25 * math.cos(math.radians(self.angle))
        self.yp = 25 + yp - 25 * math.sin(math.radians(self.angle))
        self.dx = speed * math.cos(math.radians(self.angle))
        self.dy = speed * -math.sin(math.radians(self.angle))
        self.red = 255
        self.blue = 1
        self.aux = 6

    def draw(self):
        pygame.draw.rect(screen, (self.red, 0, self.blue), (self.xp - 10, self.yp - 10, 10, 2))
        self.blue += self.aux
        self.red -= self.aux

        if self.blue >= 255 or self.blue <= 0:
            self.blue = 1
        if self.red <= 0 or self.red >= 255:
            self.red = 255

    def move(self):
        self.rect = pygame.Rect(self.xp, self.yp, 10, 2)
        self.xp = self.xp + self.dx
        self.yp = self.yp + self.dy
        self.draw()

        # bullet limit
        if self.xp >= 1180 or self.xp <= 120 or self.yp < 130 or self.yp > 700:
            self.yp = -50

    def get_data(self):
        rect = pygame.Rect(self.xp, self.yp, 10, 2)
        return rect, self.count
