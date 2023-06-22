import turtle
import winsound

win = turtle.Screen()
win.title('pong'.upper())
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)
# ^^wont refresh the screen



# P1 Paddle
p1_paddle = turtle.Turtle()
p1_paddle.speed(0)
p1_paddle.shape("square")
p1_paddle.color("red")
p1_paddle.shapesize(stretch_wid=5, stretch_len=1)
p1_paddle.penup()
p1_paddle.goto(-350, 0)

# P2 Paddle
p2_paddle = turtle.Turtle()
p2_paddle.speed(0)
p2_paddle.shape("square")
p2_paddle.color("blue")
p2_paddle.shapesize(stretch_wid=5, stretch_len=1)
p2_paddle.penup()
p2_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .16
ball.dy = .16

#score
score_p1 = 0
score_p2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: " + str(score_p1) + "  " + "Player 2: " + str(score_p2), align="center", font=("courier", 24, 'normal'))

# P1 Up Function
def p1_paddle_up():
    y = p1_paddle.ycor()
    y += 20
    p1_paddle.sety(y)

# P1 down function
def p1_paddle_down():
    y = p1_paddle.ycor()
    y -= 20
    p1_paddle.sety(y)

    # P2 down function
def p2_paddle_up():
    y = p2_paddle.ycor()
    y += 20
    p2_paddle.sety(y)

    # P2 down function
def p2_paddle_down():
    y = p2_paddle.ycor()
    y -= 20
    p2_paddle.sety(y)

def wall_sound():
    winsound.Beep(500,25)
    winsound.Beep(750,25)

def paddle_sound():
    winsound.Beep(750,25)
    winsound.Beep(500,25)

def score():
    winsound.Beep(750, 155)
    winsound.Beep(1000, 250)

# KeyBoard binding
win.listen()
win.onkeypress(p1_paddle_up, "w")
win.onkeypress(p1_paddle_down, "s")
win.onkeypress(p2_paddle_up, "Up")
win.onkeypress(p2_paddle_down, "Down")

# Main game loop
while True:
    win.update()

#   Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#   Border checking y coord posotive
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        wall_sound()

#   Border checking y coord negative
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        wall_sound()

#   Border checking x coord posostive
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_p1 += 1
        pen.clear()
        pen.write("Player 1: " + str(score_p1) + "  " + "Player 2: " + str(score_p2), align="center", font=("courier", 24, 'normal'))
        score()

#   Border checking x coord negative
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_p2 += 1
        pen.clear()
        pen.write("Player 1: " + str(score_p1) + "  " + "Player 2: " + str(score_p2), align="center", font=("courier", 24, 'normal'))
        score()

 #     Collisions p1
    if ball.xcor() < -340 and (ball.ycor() < p1_paddle.ycor() + 50) and (ball.ycor() > p1_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        paddle_sound()

#     Collisions p2
    if ball.xcor() > 340 and (ball.ycor() < p2_paddle.ycor() + 50) and (ball.ycor() > p2_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        paddle_sound()

#     paddle bottom collision p1
    if p1_paddle.ycor() - 50 < -300:
        p1_paddle.goto(-350, -249)

#     paddle bottom collision p1
    if p1_paddle.ycor() + 50 > 300:
        p1_paddle.goto(-350, 249)

#     paddle bottom collision p1
    if p2_paddle.ycor() - 50 < -300:
        p2_paddle.goto(350, -249)

#     paddle bottom collision p1
    if p2_paddle.ycor() + 50 > 300:
        p2_paddle.goto(350, 249)
