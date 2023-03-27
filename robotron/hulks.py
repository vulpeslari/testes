import pygame
from random import choice


class Hulks:
    def __init__(self, coordinates, screen, list_image, w_h):
        self.coordinates = list(coordinates)
        self.screen = screen
        self.list = list_image
        self.image = list_image[0]
        self.surface = pygame.transform.scale(self.image, (w_h, w_h))
        self.value = 0
        self.w_h = w_h
        self.speed = 0.5
        self.time = 0
        self.movement = [1, 2, 3, 4, 6, 7, 8]
        self.moving = choice(self.movement)

    def control_time(self):
        if self.time > 500:
            self.time = 0
        else:
            self.time += 1

    def goal(self):
        self.moving = choice(self.movement)

    def locomotion(self):
        if self.time == 500:
            self.moving = choice(self.movement)
        elif self.coordinates[0] >= 1150:
            self.moving = choice([3, 4, 6])
        elif self.coordinates[0] <= 110:
            self.moving = choice([5, 1, 2])
        elif self.coordinates[1] >= 650:
            self.moving = choice([8, 4, 2])
        elif self.coordinates[1] <= 110:
            self.moving = choice([7, 1, 3])

        if self.moving == 1:
            self.coordinates[0] += self.speed
            self.coordinates[1] += self.speed
            sprites = [3, 6, 7]
            self.animation(sprites)

        elif self.moving == 2:
            self.coordinates[0] += self.speed
            self.coordinates[1] -= self.speed
            sprites = [3, 6, 7]
            self.animation(sprites)

        elif self.moving == 3:
            self.coordinates[0] -= self.speed
            self.coordinates[1] += self.speed
            sprites = [3, 1, 0]
            self.animation(sprites)

        elif self.moving == 4:
            self.coordinates[0] -= self.speed
            self.coordinates[1] -= self.speed
            sprites = [0, 1, 2]
            self.animation(sprites)

        elif self.moving == 5:
            self.coordinates[0] += self.speed
            sprites = [3, 5, 4]
            self.animation(sprites)

        elif self.moving == 6:
            self.coordinates[0] -= self.speed
            sprites = [2, 1, 0]
            self.animation(sprites)

        elif self.moving == 7:
            self.coordinates[1] += self.speed
            sprites = [3, 4, 5]
            self.animation(sprites)

        elif self.moving == 8:
            self.coordinates[1] -= self.speed
            sprites = [3, 4, 5]
            self.animation(sprites)

    def animation(self, sprites):
        if self.value >= len(sprites):
            self.value = 0
        else:
            self.image = self.list[sprites[self.value]]

        self.surface = pygame.transform.scale(self.image, (self.w_h, self.w_h))
        self.value += 1

    def draw(self):
        self.screen.blit(self.surface, (self.coordinates[0], self.coordinates[1], self.w_h, self.w_h))

    def get_rect(self):
        rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.w_h, self.w_h)
        return rect
