import turtle

# draw screen
screen = turtle.Screen()
screen.title("Blackout")
screen.bgcolor("black")
screen.setup(width=800, height=1200)
screen.tracer(0)

# draw window
window = turtle.Turtle()
window.speed(0)
window.shape("square")
window.width(5)
window.color("white")
window.penup()
window.setpos(-390, 590)
window.pendown()
window.rt(90)
window.fd(1180)
window.lt(90)
window.color("blue")
window.goto(390, -590)
window.color("white")
window.lt(90)
window.fd(1180)
window.setpos(-390, 560)
window.begin_fill()
window.rt(90)
window.fd(780)
window.lt(90)
window.fd(100)
window.lt(90)
window.fd(780)
window.lt(100)
window.end_fill()
window.penup()
window.hideturtle()


# draw paddle
def draw_paddle(paddle, y, x, dye):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(dye)
    paddle.shapesize(stretch_wid=0.5, stretch_len=2.5)
    paddle.penup()
    paddle.goto(x, y)


# draw paddle
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -400, 0, 'white')

# draw bricks
bricks = turtle.Turtle()
color_list = ["red", "orange", "green", "yellow"]


def create_bricks(x, color):
    bricks.penup()
    bricks_copy = bricks.clone()
    bricks_copy.setpos(x, y)
    bricks_copy.shape("square")
    bricks_copy.shapesize(stretch_wid=0.5, stretch_len=2.5)
    bricks_copy.color(color)
    bricks_copy.clone()
    bricks_copy.goto(x - 55, y)
    return bricks_copy

y = 300
cont_color = 0
for j in range(8):
    x = 360
    color = ""
    if j % 2 != 0:
        cont_color += 1
        color = color_list[cont_color - 1]
        create_bricks(360, color)
    x -= 55
    y -= 7

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
    hud.clear()
    hud.write("{}".format(score), align="center", font=("Press Start 2P", 40, "bold"))
    ball.goto(0, 0)
    ball.dx *= -1


# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(-300, 500)
hud.write("0000", align="center", font=("Press Start 2P", 40, "bold"))


def paddle_right(paddle):
    x = paddle.xcor()
    if x < 375:
        x += 30
    else:
        x = 375
    return paddle.setx(x)


def paddle_left(paddle):
    x = paddle.xcor()
    if x > -375:
        x -= 30
    else:
        x = -375
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

    # collision with the left wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    # collision with lower wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # collision with down wall
    if ball.ycor() < -580:
        score += 1
        score_point()

    # collision with upper wall
    if ball.ycor() > 580:
        ball.setx(580)
        ball.dy *= -1

    # collision with the paddle 1
    if ball.ycor() < -375 and paddle_1.xcor() + 10 > ball.xcor() > paddle_1.xcor() - 10:
        ball.sety(-375)
        ball.dy *= -1

    # collision with the paddle 2
    if ball.ycor() > 375 and bricks.xcor() + 5 > ball.xcor() > bricks.xcor() - 5:
        ball.sety(375)
        ball.dy *= -1
