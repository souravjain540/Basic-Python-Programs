import turtle as t
playerAscore = 0
playerBscore = 0

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
rightpaddle.goto(350, 0)  # Adjusted the initial position of the right paddle

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2
ballydirection = 0.2

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
    y = y + 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 20
    leftpaddle.sety(y)

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 20
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
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Handling the collisions with paddles.

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")
