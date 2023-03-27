import pygame

from config import *
from bullets import Bullet


class Human:
    def __init__(self, list_sprites, xp, yp, width, height):
        self.list = list_sprites
        self.sprite = self.list[4]
        self.surface = pygame.transform.scale(self.sprite, (width, height))
        self.xp = xp
        self.yp = yp
        self.weight = width
        self.height = height
        self.value = 0
        self.bullets = 0
        self.bullet_move = 0

    def control(self, keys, touch_keys):
        self.move(keys, touch_keys)

    def move(self, keys, player_keys):
        # locomoção convencional, ou seja, esquerda ,direita, para cima e para baixo
        if keys[player_keys[0]] and self.xp > 100:
            self.xp -= velocity
            sprites = [4,0, 1]
            self.sprites(sprites)
        elif keys[player_keys[1]] and self.xp < 1150:
            self.xp += velocity
            sprites = [4, 2, 3]
            self.sprites(sprites)
        elif keys[player_keys[2]] and self.yp > 110:
            self.yp -= velocity
            sprites = [4, 5, 6]
            self.sprites(sprites)
        elif keys[player_keys[3]] and self.yp < 650:
            self.yp += velocity
            sprites = [6, 7, 8]
            self.sprites(sprites)
        # locomoção pelas laterais
        if keys[player_keys[0]] and keys[player_keys[2]] and (self.xp > 100 and self.yp > 110):
            self.xp -= velocity
            self.yp -= velocity
            sprites = [0, 1, 2]
            self.sprites(sprites)
        elif keys[player_keys[0]] and keys[player_keys[3]] and self.xp > 100 and self.yp < 650:
            self.xp -= velocity
            self.yp += velocity
            sprites = [0, 2, 1]
            self.sprites(sprites)
        elif keys[player_keys[1]] and keys[player_keys[2]] and self.xp < 1150 and self.yp > 110:
            self.xp += velocity
            self.yp -= velocity
            sprites = [4, 2, 3]
            self.sprites(sprites)
        elif keys[player_keys[1]] and keys[player_keys[3]] and self.xp < 1150 and self.yp < 650:
            self.xp += velocity
            self.yp += velocity
            sprites = [4, 2, 3]
            self.sprites(sprites)
        else:
            screen.blit(self.surface, (self.xp, self.yp, self.weight, self.height))

    def sprites(self, sprites):
        if self.value >= len(sprites):
            self.value = 0
        else:
            self.sprite = self.list[sprites[self.value]]

        self.surface = pygame.transform.scale(self.sprite, (self.weight, self.height))
        self.value += 1

    def draw(self):
        screen.blit(self.surface, (self.xp, self.yp, self.weight, self.height))

    def shot_bullet(self, direction):
        self.bullets = Bullet(self.xp, self.yp, direction)
        return self.bullets

    def get_rect(self):
        rect = pygame.Rect(self.xp, self.yp, self.weight, self.height)
        return rect
