import turtle


# draw screen
screen = turtle.Screen()
screen.title("Blackout")
screen.bgcolor("black")
screen.setup(width=800, height=1200)
screen.tracer(0)


# draw paddle
def draw_paddle(paddle, y, x, dye):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(dye)
    paddle.shapesize(stretch_wid=0.5, stretch_len=2.5)
    paddle.penup()
    paddle.goto(x, y)


# draw paddle 1
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -400, 0, 'white')

# draw paddle 2
paddle_2 = turtle.Turtle()
color_list = ["red", "orange", "green", "yellow"]
cont_color = 0
y = 300
for j in range(8):
    x = 375
    color = ""
    if j % 2 != 0:
        cont_color += 1
        color = color_list[cont_color - 1]
    for i in range(10):
        paddle_copy = paddle_2.clone()
        draw_paddle(paddle_copy, y, x, color)
        x -= 25
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
score_1 = 0
score_2 = 0


def score_point():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1


# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 600)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


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
        score_2 += 1
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
    if ball.ycor() > 375 and paddle_2.xcor() + 5 > ball.xcor() > paddle_2.xcor() - 5:
        ball.sety(375)
        ball.dy *= -1
