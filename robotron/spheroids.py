import pygame
from random import choice
from enforcers import Enforcers
from sprites import enforcers_s


class Spheroids:
    def __init__(self, coordinates, screen, list_image, w_h):
        self.coordinates = list(coordinates)
        self.screen = screen
        self.dx = 0
        self.dy = 0
        self.list = list_image
        self.image = list_image[0]
        self.surface = pygame.transform.scale(self.image, (w_h, w_h))
        self.value = 0
        self.w_h = w_h
        self.speed = 5
        self.time = 0
        self.movement = [self.speed, self.speed * -1]
        self.aux = []
        self.list_enforcers = []
        self.end = False
        self.qtd = 0

    def enforcers(self):
        return self.list_enforcers

    def delete(self):
        return self.end

    def control_enforcers(self):
        self.list_enforcers.clear()

    def locomotion(self):
        if self.time <= 200 and self.time % 100 == 0:
            self.dx = choice(self.movement)
            self.dy = choice(self.movement)
            self.aux = [0, 1, 2, 3, 4, 5]
        elif 200 < self.time < 600 and self.time % 100 == 0:
            self.dx = choice(self.movement)
            self.dy = choice(self.movement)
            self.aux = [0, 1, 2, 3, 4, 5]
            self.list_enforcers.append(Enforcers(self.coordinates, self.screen,  enforcers_s, self.w_h))

        elif self.time > 605:
            self.end = True
        elif self.coordinates[0] >= 1150:
            self.dx = -self.speed
            self.dy = choice(self.movement)
        elif self.coordinates[0] <= 110:
            self.dx = self.speed
            self.dy = choice(self.movement)
        elif self.coordinates[1] >= 670:
            self.dy = -self.speed
            self.dx = choice(self.movement)
        elif self.coordinates[1] <= 100:
            self.dy = self.speed
            self.dx = choice(self.movement)

        self.coordinates[0] += self.dx
        self.coordinates[1] += self.dy
        self.time += 1
        self.delete()
        self.animation(self.aux)


    def animation(self, sprites):
        if self.value >= len(sprites):
            self.value = 0
        else:
            self.image = self.list[sprites[self.value]]

        self.surface = pygame.transform.scale(self.image, (self.w_h, self.w_h))
        self.value += 1

    def draw(self):
        self.screen.blit(self.surface, (self.coordinates[0], self.coordinates[1], self.w_h, self.w_h))
