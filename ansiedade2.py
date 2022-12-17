import turtle

# draw screen
screen = turtle.Screen()
screen.title("Blackout")
screen.bgcolor("black")
screen.setup(width=400, height=600)
screen.tracer(0)
# positions of each brick from wall
position_brick = []
# draw window
window = turtle.Turtle()
window.speed(0)
window.shape("square")
window.width(5)
window.color("white")
window.penup()
window.setpos(-295, 490)
window.pendown()
window.rt(90)
window.fd(1180)
window.lt(90)
window.color("blue")
window.goto(340, -490)
window.color("white")
window.lt(90)
window.fd(1180)
window.penup()
window.hideturtle()


# draw paddle
def draw_paddle(paddle, y, x, dye):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(dye)
    paddle.shapesize(stretch_wid=0.4, stretch_len=2)
    paddle.penup()
    paddle.goto(x, y)


# draw paddle
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -300, 0, 'blue')

# draw bricks
bricks = turtle.Turtle()
color_list = ["red", "orange", "green", "yellow"]


def create_bricks(x, color):
    bricks.penup()
    bricks_copy = bricks.clone()
    bricks_copy.setpos(x, y)
    bricks_copy.shape("square")
    bricks_copy.shapesize(stretch_wid=0.4, stretch_len=2)
    bricks_copy.color(color)
    bricks_copy.clone()
    bricks_copy.setx(x - 45)
    position_brick.append(bricks_copy.position())
    return bricks_copy


y = 200
cont_color = 0
brick_lane = []
for i in range(8):
    x = 315
    color = ""
    if i % 2 != 0:
        cont_color += 1
        color = color_list[cont_color - 1]
    else:
        color = color_list[cont_color]
    for j in range(13):
        create_bricks(x, color)
        brick_lane.append(bricks)
        x -= 45
    y -= 12

print(position_brick)
print(len(position_brick))
print(position_brick[0][0])
print(brick_lane)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(0.5)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -1
ball.dy = -1

# score
score = 0


def score_point():
    hud_left.clear()
    hud_left.write("{}".format(score), align="center", font=("Press Start 2P", 40, "bold"))
    ball.goto(0, 0)
    ball.dx *= -1


# head-up display
def head(hud, x, y):
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(x, y)
    hud.write("0000", align="center", font=("Press Start 2P", 50, "bold"))


hud_left = turtle.Turtle()
head(hud_left, -180, 250)

hud_right = turtle.Turtle()
head(hud_right, 220, 250)


def paddle_right(paddle):
    x = paddle.xcor()
    if x < 315:
        x += 25
    else:
        x = 315
    return paddle.setx(x)


def paddle_left(paddle):
    x = paddle.xcor()
    if x > -270:
        x -= 25
    else:
        x = -270
    return paddle.setx(x)


# keyboard
screen.listen()
screen.onkeypress(lambda: paddle_right(paddle_1), "Right")
screen.onkeypress(lambda: paddle_left(paddle_1), "Left")

while True:
    screen.update()

    # ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # collision with the right wall
    if ball.xcor() > 335:
        ball.setx(335)
        ball.dx *= -1

    # collision with left wall
    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1

    # collision with lower wall
    if ball.ycor() < -370:
        score += 1
        score_point()


    # collision with the brick
    if ball.ycor() > position_brick[-1][0] - 5:
        for i in range(len(position_brick)):
            position_x = position_brick[i][0]
            position_y = position_brick[i][1]
            if ball.ycor() == position_y and position_x + 26 > ball.xcor() > position_x - 26:
                ball.sety(position_y)
                ball.dy *= -1
                break

    # collision with the paddle
    if ball.ycor() < -290 and paddle_1.xcor() + 10 > ball.xcor() > paddle_1.xcor() - 10:
        ball.sety(-290)
        ball.dy *= -1
