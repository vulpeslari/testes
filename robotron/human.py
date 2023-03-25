from config import *
from bullet import Bullet


class Human:
    def __init__(self, list_sprites, xp, yp, width, height):
        self.list = list_sprites
        self.sprite = self.list[6]
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
        # locomoção convencional, ou seja, esquerda,
        # direita, para cima e para baixo
        if keys[player_keys[0]] and self.xp > 100:
            self.xp -= velocity
            sprites = [0, 1, 2]
            self.sprites(sprites)
            self.bullet_move = 180
        elif keys[player_keys[1]] and self.xp < 1150:
            self.xp += velocity
            sprites = [2, 3, 4]
            self.sprites(sprites)
            self.bullet_move = 0
        elif keys[player_keys[2]] and self.yp > 110:
            self.yp -= velocity
            sprites = [9, 10, 11]
            self.sprites(sprites)
            self.bullet_move = 90
        elif keys[player_keys[3]] and self.yp < 650:
            self.yp += velocity
            sprites = [6, 7, 8]
            self.sprites(sprites)
            self.bullet_move = -90
        # locomoção pelas laterais
        if keys[player_keys[0]] and keys[player_keys[2]] and (self.xp > 100 and self.yp > 110):
            self.xp -= velocity
            self.yp -= velocity
            sprites = [0, 1, 2]
            self.sprites(sprites)
            self.bullet_move = 150
        elif keys[player_keys[0]] and keys[player_keys[3]] and self.xp > 100 and self.yp < 650:
            self.xp -= velocity
            self.yp += velocity
            sprites = [0, 2, 1]
            self.sprites(sprites)
            self.bullet_move = -150
        elif keys[player_keys[1]] and keys[player_keys[2]] and self.xp < 1150 and self.yp > 110:
            self.xp += velocity
            self.yp -= velocity
            sprites = [3, 4, 5]
            self.sprites(sprites)
            self.bullet_move = 30
        elif keys[player_keys[1]] and keys[player_keys[3]] and self.xp < 1150 and self.yp < 650:
            self.xp += velocity
            self.yp += velocity
            sprites = [3, 5, 4]
            self.sprites(sprites)
            self.bullet_move = -30
        else:
            screen.blit(self.surface, (self.xp, self.yp, self.weight, self.height))

    def sprites(self, sprites):
        if self.value >= len(sprites):
            self.value = 0
        else:
            self.sprite = self.list[sprites[self.value]]

        self.surface = pygame.transform.scale(self.sprite, (self.weight, self.height))
        print(self.value)
        self.value += 1

    def draw(self):
        screen.blit(self.surface, (self.xp, self.yp, self.weight, self.height))

    def shot_bullet(self):
        self.bullets = Bullet(self.xp, self.yp, self.bullet_move)
        return self.bullets

