from math import cos, radians
from config import *


class Bullet:
    def __init__(self, xp, yp, direction):
        self.count = 0
        self.direction = direction
        self.rect = None
        self.xp = 20 + xp
        self.yp = 20 + yp
        self.dx = 5
        self.dy = 5
        self.red = 255
        self.blue = 1
        self.aux = 6

    def draw(self, w, h, situation):
        if situation == 1:
            pygame.draw.rect(screen, (self.red, 0, self.blue), (self.xp, self.yp, w, h))
        elif situation == 2:
            pygame.draw.line(screen, (self.red, 0, self.blue), (self.xp, self.yp),
                             (self.xp + 7.071067812, self.yp + 7.071067812), 5)
        elif situation == 3:
            pygame.draw.line(screen, (self.red, 0, self.blue), (self.xp, self.yp),
                             (self.xp - 7.071067812, self.yp - 7.071067812), 5)
        elif situation == 4:
            pygame.draw.line(screen, (self.red, 0, self.blue), (self.xp, self.yp),
                             (self.xp + 7.071067812, self.yp - 7.071067812), 5)
        elif situation == 5:
            pygame.draw.line(screen, (self.red, 0, self.blue), (self.xp, self.yp),
                             (self.xp - 7.071067812, self.yp + 7.071067812), 5)
        self.blue += self.aux
        self.red -= self.aux

        if self.blue >= 255 or self.blue <= 0:
            self.blue = 1
        if self.red <= 0 or self.red >= 255:
            self.red = 255

    def move(self):
        w = 3
        h = 10
        if self.direction == 'l':
            self.xp -= self.dx
            self.draw(h, w, 1)
        elif self.direction == 'r':
            self.xp += self.dx
            self.draw(h, w, 1)
        elif self.direction == 'up':
            self.yp -= self.dy
            self.draw(w, h, 1)
        elif self.direction == 'dw':
            self.yp += self.dy
            self.draw(w, h, 1)
        elif self.direction == 'rdw':
            self.yp += self.dy
            self.xp += self.dx
            self.draw(w, h, 2)
        elif self.direction == 'lup':
            self.yp -= self.dy
            self.xp -= self.dx
            self.draw(w, h, 3)
        elif self.direction == 'rup':
            self.yp -= self.dy
            self.xp += self.dx
            self.draw(w, h, 4)
        elif self.direction == 'ldw':
            self.yp += self.dy
            self.xp -= self.dx
            self.draw(w, h, 5)

        # bullet limit
        if self.xp >= 1180 or self.xp <= 120 or self.yp < 130 or self.yp > 700:
            self.yp = -50

    def get_data(self):
        rect = pygame.Rect(self.xp, self.yp, 10, 2)
        return rect
