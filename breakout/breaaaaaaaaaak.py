import pygame

pygame.init()

# color palette
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 97, 148)
red = (162, 8, 0)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

# screen
size = (460, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")

# score text
score_font = pygame.font.Font('PressStart2P.ttf', 44)
score_text = score_font.render('000', True, white, black)
score_text_rect = score_text.get_rect()
score_text_rect.center = (100, 120)

# player text
player_font = pygame.font.Font('PressStart2P.ttf', 44)
player_text = player_font.render('1', True, white, black)
player_text_rect = player_text.get_rect()
player_text_rect.center = (55, 60)

# death text
death_font = pygame.font.Font('PressStart2P.ttf', 44)
death_text = death_font.render('1', True, white, black)
death_text_rect = death_text.get_rect()
death_text_rect.center = (325, 60)

# point text
point_font = pygame.font.Font('PressStart2P.ttf', 44)
point_text = score_font.render('000', True, white, black)
point_text_rect = point_text.get_rect()
point_text_rect.center = (370, 120)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('bleep_sound.wav')

# player 1
paddle = pygame.image.load("player.png")
paddle_x = 50
paddle_left = False
paddle_right = False

# ball
ball = pygame.image.load("ball.png")
ball_x = 250
ball_y = 325
ball_dx = 5
ball_dy = 5

# score
score = 0
score_death = 1
count_brick = 0

# game loop
game_start = True
game_clock = pygame.time.Clock()

while game_start:

    # quit option
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_start = False

        # key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_left = True
            if event.key == pygame.K_RIGHT:
                paddle_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_left = False
            if event.key == pygame.K_RIGHT:
                paddle_right = False

    # clear screen
    screen.fill(black)

    # create brick lane
    brick_x = [10, 42, 74, 106, 138, 170, 202, 234, 266, 298, 330, 362, 394, 426]
    brick_y = [180, 191, 202, 213, 224, 235, 246, 257]

    brick_lane = []
    for i in brick_x:
        for j in brick_y:
            if j == 180 or j == 191:
                brick = pygame.image.load("red.png").convert()
                screen.blit(brick, (i, j))
                brick_lane.append(brick)

            elif j == 202 or j == 213:
                brick = pygame.image.load("orange.png").convert()
                screen.blit(brick, (i, j))
                brick_lane.append(brick)

            elif j == 224 or j == 235:
                brick = pygame.image.load("green.png").convert()
                screen.blit(brick, (i, j))
                brick_lane.append(brick)

            elif j == 246 or j == 257:
                brick = pygame.image.load("yellow.png").convert()
                screen.blit(brick, (i, j))
                brick_lane.append(brick)


    # ball collisions with the walls
    if ball_x > 440:
        ball_dx *= -1
        bounce_sound_effect.play()

    if ball_x <= 0:
        ball_dx *= -1
        bounce_sound_effect.play()

    if ball_y < 15:
        ball_dy *= -1
        bounce_sound_effect.play()

    if ball_y > 590:
        score_death += 1
        ball_x = 225
        ball_y = 300

        if score_death > 4:
            game_start = False

    # ball collision with the paddle
    if 550 < ball_y > 535:
        if paddle_x - 20 < ball_x - 5:
            if paddle_x + 20 > ball_x - 20:
                ball_dy *= -1
                bounce_sound_effect.play()

    # ball collision with the bricks


    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # paddle right movement
    if paddle_x > 0:
        if paddle_left:
            paddle_x -= 5
        else:
            paddle_x += 0

    # paddle left movement
    if paddle_x < 405:
        if paddle_right:
            paddle_x += 5
        else:
            paddle_x += 0

    # update score hud
    score_text = score_font.render(str(score), True, white, black)
    death_text = death_font.render(str(score_death), True, white, black)

    # drawing objects
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(paddle, (paddle_x, 550))
    screen.blit(score_text, score_text_rect)
    screen.blit(death_text, death_text_rect)
    screen.blit(player_text, player_text_rect)
    screen.blit(point_text, point_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
