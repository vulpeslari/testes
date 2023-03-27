from config import *
from score import Score
from human import Human
from hulks import Hulks
from grunts import Grunts
from sprites import *
from spheroids import Spheroids
import random

game_loop = True

point = 0

score = Score(point, 120, 85, (255, 255, 255))

boy = Human(player, 650, 410, 40, 40, )
clock = pygame.time.Clock()
create = True

list_grunts = []
list_hulks = []
list_family = []
list_spheroids = []
list_enforcers = []
lista = positions.copy()
bullets = []
time = 0
while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_loop = False
            if event.key == pygame.K_c:
                bullets.append(boy.shot_bullet('rdw'))
            elif event.key == pygame.K_q:
                bullets.append(boy.shot_bullet('lup'))
            elif event.key == pygame.K_e:
                bullets.append(boy.shot_bullet('rup'))
            elif event.key == pygame.K_z:
                bullets.append(boy.shot_bullet('ldw'))
            elif event.key == pygame.K_a:
                bullets.append(boy.shot_bullet('l'))
            elif event.key == pygame.K_d:
                bullets.append(boy.shot_bullet('r'))
            elif event.key == pygame.K_w:
                bullets.append(boy.shot_bullet('up'))
            elif event.key == pygame.K_s:
                bullets.append(boy.shot_bullet('dw'))

    keys = pygame.key.get_pressed()
    boy.control(keys, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
    boy.draw()

    if create:
        for i in range(5):
            a = random.choice(lista)
            spheroid = Spheroids(a, screen, spheroids_s, 40)
            grunts = Grunts(a, screen, grunts_s, 40)
            hulks = Hulks(a, screen, hulks_s, 40)
            family = Hulks(a, screen, random.choice([boy_s, girl, kid]),40)
            lista.remove(a)
            list_spheroids.append(spheroid)
            list_family.append(family)
            list_hulks.append(hulks)
            list_grunts.append(grunts)

        create = False

    for x in list_spheroids:
        x.locomotion()
        x.draw()
        list_enforcers = list_enforcers + x.enforcers()
        x.control_enforcers()
        if x.delete():
            list_spheroids.remove(x)

    for x in list_enforcers:
        x.locomotion([boy.xp, boy.yp])
    for x in list_hulks:
        x.locomotion()
        x.draw()
    for y in list_family:
        y.locomotion()
        y.draw()
    
    for x in list_grunts:
        x.locomotion([boy.xp, boy.yp])
        x.draw()


    for b in bullets:
        b.move()
        for x in list_grunts:
            if b.get_data().colliderect(x.get_rect()):
                list_grunts.remove(x)
                bullets.remove(b)
        for x in list_hulks:
            if b.get_data().colliderect(x.get_rect()):
                x.goal()
                bullets.remove(b)
    for x in list_family:
        if boy.get_rect().colliderect(x.get_rect()):
            list_family.remove(x)
            point += 1
            score.upload_score(point)

    arena.run()
    score.draw(screen)
    pygame.display.update()
    screen.fill("#000000")
    clock.tick(30)
    time += 1


