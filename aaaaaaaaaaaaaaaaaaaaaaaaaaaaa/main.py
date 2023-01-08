import pygame
import math

pygame.init()

# Creating the window and naming the game
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Breakout")

# Defining sound effects
bounce_sound = pygame.mixer.Sound('bounce.wav')
brick_sound = pygame.mixer.Sound('brick_sound.wav')

# Color list
blue = (77, 109, 243)
red = (162, 8, 0)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

# Defining the objects
drawGroup = pygame.sprite.Group()
edge = pygame.sprite.Sprite(drawGroup)
paddle = pygame.sprite.Sprite(drawGroup)
ball = pygame.sprite.Sprite(drawGroup)


def draw_objects(obj, w, h, x_cor, y_cor, data):
    obj.image = pygame.image.load(data)
    obj.image = pygame.transform.scale(obj.image, [w, h])
    obj.rect = pygame.Rect(x_cor, y_cor, 0, 0)


def hud_draw(x_cor, y_cor, score, size, bst):
    font = pygame.font.Font('PressStart2P.ttf', size)
    if bst:
        score = str(score).zfill(3)
    text = font.render(f"{score}", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x_cor, y_cor)
    screen.blit(text, text_rect)


def draw_border_details():
    pygame.draw.line(screen, blue, (24, 700), (24, 725), 12)
    pygame.draw.line(screen, blue, (576, 700), (576, 725), 12)
    pygame.draw.line(screen, red, (24, 180), (24, 207), 12)
    pygame.draw.line(screen, red, (576, 180), (576, 207), 12)
    pygame.draw.line(screen, orange, (24, 208), (24, 237), 12)
    pygame.draw.line(screen, orange, (576, 208), (576, 237), 12)
    pygame.draw.line(screen, green, (24, 238), (24, 267), 12)
    pygame.draw.line(screen, green, (576, 238), (576, 267), 12)
    pygame.draw.line(screen, yellow, (24, 268), (24, 296), 12)
    pygame.draw.line(screen, yellow, (576, 268), (576, 296), 12)


# Drawing the objects
draw_objects(edge, 600, 900, 7, 0, "Edge.png")
draw_objects(paddle, 35, 10, 270, 700, "Paddle.png")
draw_objects(ball, 8, 8, 298, 470, "Ball.png")

# Drawing the bricks
colors = ['YellowBrick', 'YellowBrick', 'GreenBrick', 'GreenBrick',
          'OrangeBrick', 'OrangeBrick', 'RedBrick', 'RedBrick']
bricks_count = []
x_pos = []
y_pos = []
y = 300

for i in range(8):
    y = y - 15
    x = 30
    for j in range(14):
        brick = pygame.sprite.Sprite(drawGroup)
        brick.image = pygame.image.load(f"{colors[i]}.png")
        brick.image = pygame.transform.scale(brick.image, [35, 11])
        brick.rect = pygame.Rect(x, y, 0, 0)
        x_pos.append(x)
        y_pos.append(y)
        bricks_count.append(brick)

        x += 39

# Initial scores
birth_score = 1
brick_score = 0

# Initial ball coordinates
ball_dx = 3
ball_dy = 3

# Game looping
game_loop = True
game_restart = True
count_brick = 0
while game_loop:

    for event in pygame.event.get():

        # Command to close the game
        if event.type == pygame.QUIT:
            game_loop = False

    # Paddle moves
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.rect.x > 31:
        paddle.rect.x -= 5
    elif keys[pygame.K_RIGHT] and paddle.rect.x < 535:
        paddle.rect.x += 5

    # Ball movement
    ball.rect.x += ball_dx
    ball.rect.y += ball_dy

    # Collision with the right wall
    if ball.rect.x >= 565:
        ball_dx *= -1
        bounce_sound.play()

    # Collision with the left wall
    if ball.rect.x <= 25:
        ball_dx *= -1
        bounce_sound.play()

    # Collision with the roof
    if ball.rect.y <= 15:
        ball_dy *= -1
        bounce_sound.play()
        ball_dy = 5
        ball_dx = 5

    # Collision with the paddle
    if 700 > ball.rect.y > (paddle.rect.y - 5) and paddle.rect.x + 30 > ball.rect.x > paddle.rect.x - 30:
        ball_dy *= -1
        bounce_sound.play()
        if ball.rect.x < paddle.rect.x + 10:
            ball_dy += math.sin(math.radians(30))
        if ball.rect.x > paddle.rect.x - 10:
            ball_dy += math.sin(math.radians(120))

    # Collision with the floor
    if ball.rect.y > paddle.rect.y + 100:
        ball.rect.y = 470
        ball.rect.x = 298
        birth_score += 1
        ball_dy = 2
        ball_dx = 2

    # Collision with the brick
    if birth_score <= 4:
        for brick in bricks_count:
            if brick.rect.y > ball.rect.y > brick.rect.y - 10 \
                    and brick.rect.x + 40 > ball.rect.x > brick.rect.x - 40:
                brick.rect = pygame.Rect(1000, 1000, 0, 0)
                ball_dy *= -1
                brick_score += 1
                count_brick += 1
                bricks_count.remove(brick)
                bounce_sound.play()

                # Score
                if brick.rect.y > 255:
                    brick_score += 1

                elif brick.rect.y > 225:
                    brick_score += 3

                elif brick.rect.y > 195:
                    brick_score += 5

                else:
                    brick_score += 7

                # Ball speed
                if count_brick == 4:
                    ball_dy = 3.5
                    ball_dx = 3.5
                if count_brick == 12:
                    ball_dy = 4
                    ball_dx = 4
                if ball.rect.y == 237:
                    ball_dy = 4.5
                    ball_dx = 4.5

    if birth_score > 4:
        paddle.rect.x = -35
        paddle.image = pygame.transform.scale(paddle.image, [655, 25])

        for brick in bricks_count:
            if ball.rect.y < brick.rect.y + 25 and brick.rect.x + 20 > ball.rect.x > brick.rect.x - 20:
                ball_dy *= -1

        if ball.rect.y == 700:
            ball_dy *= -1

    screen.fill([0, 0, 0])

    # Draw Hud and border details
    drawGroup.draw(screen)
    draw_border_details()

    if len(bricks_count) == 112:
        hud_draw(80, 60, '1', 50, 0)
        hud_draw(130, 140, '000', 50, 0)
        hud_draw(440, 60, birth_score, 50, 0)
        hud_draw(470, 140, '000', 50, 0)

    else:
        hud_draw(80, 60, '1', 50, 0)
        hud_draw(130, 140, brick_score, 50, 1)
        hud_draw(440, 60, birth_score, 50, 0)
        hud_draw(470, 140, '000', 50, 0)

    # Game ending
    if len(bricks_count) == 0:
        hud_draw(300, 400, 'GAME IS OVER! YOU WON!', 24, 0)

    # Display update
    pygame.display.flip()
