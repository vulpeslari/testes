import pygame
from bullet_enemies import BulletEnemies


class Enforcers:
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
        self.speed = 0.8
        self.time = 0
        self.movement = [self.speed, self.speed * -1]
        self.aux = 0
        self.bullet_coordinate = [0, 0]
        self.permission = True
        self.bullets = None

    def locomotion(self, p_player):
        if p_player[0] > self.coordinates[0]:
            self.dx = self.speed
        if p_player[0] < self.coordinates[0]:
            self.dx = -self.speed
        if p_player[1] > self.coordinates[1]:
            self.dy = self.speed
        if p_player[1] < self.coordinates[1]:
            self.dy = -self.speed
        if self.time % 10 == 0 and self.time <= 60:
            self.image = self.list[self.aux]
            self.surface = pygame.transform.scale(self.image, (self.w_h, self.w_h))
            self.aux += 1

        self.coordinates[0] += self.dx
        self.coordinates[1] += self.dy
        self.time += 1
        self.draw()
        if self.time > 1000:
            self.time = 0

    def draw(self):
        self.screen.blit(self.surface, (self.coordinates[0], self.coordinates[1], self.w_h, self.w_h))
