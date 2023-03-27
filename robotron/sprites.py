import pygame

boy_s = []
for i in range(1, 13):
    boy_s.append(pygame.image.load(f"boy/boy-{i}.png"))

grunts_s = []
for i in range(1, 4):
    grunts_s.append(pygame.image.load(f"grunts/robot4-{i}.png"))

girl = []
for i in range(1, 13):
    girl.append(pygame.image.load(f"girl/girl-{i}.png"))

spheroids_s = []
for i in range(1, 8):
    spheroids_s.append(pygame.image.load(f"esferoides/sprite_{i}.png"))

enforcers_s = []
for i in range(1, 10):
    enforcers_s.append(pygame.image.load(f"enforcers/sprites_{i}.png"))
kid = []
for i in range(1, 13):
    kid.append(pygame.image.load(f"kid/kid-{i}.png"))


player = []
for i in range(1, 11):
    player.append(pygame.image.load(f"player/sprite_{i}.png"))

hulks_s = []
for i in range(1, 9):
    hulks_s.append(pygame.image.load(f"hulks/sprite_{i}.png"))

positions = []
for i in range(110, 1161, 40):
    for j in range(110, 680, 40):
        positions.append((i, j))
for i in range(670 - 80, 670 + 80, 40):
    for j in range(430 - 80, 430 + 80, 40):
        positions.remove((i, j))
