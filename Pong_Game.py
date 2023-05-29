import turtle as t
import os

player_a_score = 0
player_b_score = 0
ball_dx = 0.2
ball_dy = 0.2

# Create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_dx
ball.dy = ball_dy

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score", align="center", font=('Arial', 24, 'normal'))

# Code for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Handling the collisions with paddles.
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() - 50 < ball.ycor() < rightpaddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")
