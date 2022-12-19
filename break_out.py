import time
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
window.setpos(-295, 700)
window.pendown()
window.rt(90)
window.fd(1500)
window.lt(90)
window.goto(340, -700)
window.color("white")
window.pendown()
window.lt(90)
window.fd(1500)
window.penup()
window.goto(-295, 490)
window.pendown()
window.begin_fill()
window.fd(50)
window.rt(90)
window.fd(630)
window.rt(90)
window.fd(50)
window.rt(90)
window.fd(630)
window.end_fill()
window.penup()
window.hideturtle()


# draw object
def draw_object(obj, cor_x, cor_y, dye):
    obj.speed(0)
    obj.shape("square")
    obj.color(dye)
    obj.shapesize(stretch_wid=0.4, stretch_len=2)
    obj.penup()
    obj.goto(cor_x, cor_y)


# draw paddle
paddle_1 = turtle.Turtle()
draw_object(paddle_1, 0, -300, 'blue')

# draw ball
ball = turtle.Turtle()
draw_object(ball, 0, 0, "white")
ball.shapesize(0.5)
ball.dx = -1
ball.dy = -1

# draw bricks
bricks = turtle.Turtle()
color_list = ["red", "orange", "green", "yellow"]


def create_bricks(dye):
    bricks.penup()
    bricks_copy = bricks.clone()
    bricks_copy.shape("square")
    bricks_copy.shapesize(stretch_wid=0.4, stretch_len=2)
    bricks_copy.color(dye)
    bricks_copy.penup()
    bricks_copy.goto(j, i)
    position_brick.append(bricks_copy.position())
    brick_lane.append(bricks_copy)


# create the brick lane
brick_lane = []
y = 200
y_cor = [y for y in range(y, 115, -12)]
x = 315
x_cor = [x for x in range(x, -271, -45)]


# head-up display
def head(hud, cor_x, cor_y, head_format):
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(cor_x, cor_y)
    hud.write(head_format, align="center", font=("FixedSys", 45, "bold"))


hud_left = turtle.Turtle()
head(hud_left, -160, 250, "000")

hud_death = turtle.Turtle()
head(hud_death, 140, 350, "1")

hud_ghost = turtle.Turtle()
head(hud_ghost, -260, 350, "1")

hud_right = turtle.Turtle()
head(hud_right, 240, 250, "000")

for i in y_cor:
    color = ""
    if i == 200 or i == 188:
        color = color_list[0]
    elif i == 176 or i == 164:
        color = color_list[1]
    elif i == 152 or i == 140:
        color = color_list[2]
    elif i == 128 or i == 116:
        color = color_list[3]
    for j in x_cor:
        create_bricks(color)

# scores
score = 0
score_death = 1
count_brick = 0


def score_point(header, scoreboard):
    header.clear()
    header.write("{}".format(scoreboard), align="center", font=("FixedSys", 45, "bold"))

    if header == hud_death:
        ball.goto(0, 0)
        ball.dx *= -1

    else:
        ball.dx *= 1


# set paddle movements
def paddle_right(paddle):
    cor_x = paddle.xcor()
    if cor_x < 315:
        cor_x += 25
    else:
        cor_x = 315
    return paddle.setx(cor_x)


def paddle_left(paddle):
    cor_x = paddle.xcor()
    if cor_x > -270:
        cor_x -= 25
    else:
        cor_x = -270
    return paddle.setx(cor_x)


# keyboard
screen.listen()
screen.onkeypress(lambda: paddle_right(paddle_1), "Right")
screen.onkeypress(lambda: paddle_left(paddle_1), "Left")

game_start = True

# start game
while game_start:
    screen.update()

    # ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # ball bounce
    def bounce(situation):
        if situation == "top" or situation == "paddle":
            ball.setheading(360 - ball.heading())

        elif 180 > ball.heading() >= 0:
            ball.setheading(180 - ball.heading())

        elif 180 <= ball.heading() < 360:
            ball.setheading(540 - ball.heading())


    # collision with right wall
    if ball.xcor() > 335:
        ball.setx(335)
        ball.dx *= -1
        bounce("right")

    # collision with left wall
    if ball.xcor() < -290:
        ball.setx(-280)
        ball.dx *= -1
        bounce("left")

    # collision with lower wall
    if ball.ycor() < -370:
        score_death += 1
        score_point(hud_death, score_death)
        count_brick = 0

        if score_death > 4:
            time.sleep(3)
            screen.update()
            score_death = 0

    # collision with the upper wall
    if ball.ycor() > 435:
        ball.sety(425)
        ball.dy *= -1
        bounce("top")

    # check brick hit
    def brick_hit():
        ball.sety(position_y - 10)
        ball.dy *= -1
        brick.goto(1000, 1000)
        brick_lane.remove(brick)
        bounce("top")
        return


    # collision with the brick and their scores
    for brick in brick_lane:
        position_x = brick.xcor()
        position_y = brick.ycor()

        if ball.ycor() == position_y and position_x + 26 > ball.xcor() > position_x - 26:
            brick_hit()
            count_brick += 1

            if position_y == 200 or position_y == 188:
                score += 7
                score_point(hud_left, score)

            elif ball.ycor() > 215:
                paddle_1.shapesize(stretch_wid=0.4, stretch_len=1)

            elif position_y == 176 or position_y == 164:
                score += 5
                score_point(hud_left, score)

            elif position_y == 152 or position_y == 140:
                score += 3
                score_point(hud_left, score)

            elif position_y == 128 or position_y == 116:
                score += 1
                score_point(hud_left, score)


    # collision with the paddle
    if -315 < ball.ycor() < -285 and paddle_1.xcor() + 15 > ball.xcor() > paddle_1.xcor() - 15:
        ball.sety(-285)
        ball.dy *= -1
        bounce("paddle")
