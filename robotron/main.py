from config import *
from score import Score
from human import Human
from sprites import boy

game_loop = True
arena = Arena(screen, sc_width, sc_height)
point = 0
score = Score(point, 120, 85, (255, 255, 255))
boy = Human(boy, 650, 400, 40, 40)
clock = pygame.time.Clock()
bullets = []

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_loop = False
            if event.key == pygame.K_q:
                bullets.append(boy.shot_bullet())

    # start shot
    for b in bullets:
        b.move()

    keys = pygame.key.get_pressed()
    boy.control(keys, [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
    boy.draw()
    arena.run()
    score.draw(screen)
    pygame.display.update()
    screen.fill("#000000")
    clock.tick(50)
