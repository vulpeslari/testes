import pygame


class Grunts:
    def __init__(self, coordinates, screen, list_image, w_h):
        self.coordinates = list(coordinates)
        self.screen = screen
        self.list = list_image
        self.image = list_image[0]
        self.surface = pygame.transform.scale(self.image, (w_h, w_h))
        self.value = 0
        self.w_h = w_h
        self.speed = 0.5

    def locomotion(self, p_player):
        if p_player[0] > self.coordinates[0] and p_player[1] > self.coordinates[1]:
            self.coordinates[0] += self.speed
            self.coordinates[1] += self.speed
            sprites = [0, 1]
            self.animation(sprites)

        elif p_player[0] > self.coordinates[0] and p_player[1] < self.coordinates[1]:
            self.coordinates[0] += self.speed
            self.coordinates[1] -= self.speed
            sprites = [0, 2]
            self.animation(sprites)

        elif p_player[0] < self.coordinates[0] and p_player[1] > self.coordinates[1]:
            self.coordinates[0] -= self.speed
            self.coordinates[1] += self.speed
            sprites = [0, 1]
            self.animation(sprites)

        elif p_player[0] < self.coordinates[0] and p_player[1] < self.coordinates[1]:
            self.coordinates[0] -= self.speed
            self.coordinates[1] -= self.speed
            sprites = [0, 2]
            self.animation(sprites)

        elif p_player[0] == self.coordinates[0] and p_player[1] > self.coordinates[1]:
            self.coordinates[1] += self.speed
            sprites = [0, 1]
            self.animation(sprites)

        elif p_player[0] == self.coordinates[0] and p_player[1] < self.coordinates[1]:
            self.coordinates[1] -= self.speed
            sprites = [0]
            self.animation(sprites)

        elif p_player[1] == self.coordinates[1] and p_player[0] > self.coordinates[0]:
            self.coordinates[1] += self.speed
            sprites = [0]
            self.animation(sprites)

        elif p_player[1] == self.coordinates[1] and p_player[0] < self.coordinates[0]:
            self.coordinates[1] -= self.speed
            sprites = [0]
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
