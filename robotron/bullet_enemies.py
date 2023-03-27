from config import *


class BulletEnemies:
    def __init__(self, sprites, coordinate, dx, dy, w_h):
        self.sprites = sprites
        self.image = sprites[0]
        self.surface = pygame.transform.scale(self.image, (w_h, w_h))
        self.coordinate = [0, 0]
        self.coordinate[0] = coordinate[0]
        self.coordinate[1] = coordinate[1]
        self.w_h = w_h
        self.dx = dx * 2
        self.dy = dy * 2
        self.value = 0

    def move(self):
        self.coordinate += self.dx
        self.coordinate += self.dy

    def animation(self, sprites):
        if self.value >= len(sprites):
            self.value = 0
        else:
            self.image = self.sprites[sprites[self.value]]

        self.surface = pygame.transform.scale(self.image, (self.w_h, self.w_h))
        self.value += 1

    def draw(self):
        screen.blit(self.surface, (self.coordinate[0], self.coordinate[1], self.w_h, self.w_h))
