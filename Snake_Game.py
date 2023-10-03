import turtle
import time

# Screen Functions
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("The Snake")
screen.setup(height=600, width=600)
screen.tracer(0)

# Functions


def move_left():
    segments[-1].lt(90)


# Turtle
starting_positions = [(-20, 0), (0, 0), (20, 0)]
segments = []

for position in starting_positions:
    new_position = turtle.Turtle()
    new_position.penup()
    new_position.shape("square")
    new_position.color("white")
    new_position.setposition(position)
    new_position.speed("slowest")
    segments.append(new_position)


screen.update()
game_over = 0

while not game_over:
    for segment in segments[0:-1]:
        segment.setposition(segments[segments.index(segment)+1].position())
    screen.listen()
    screen.onkeypress(fun=move_left, key="Up")
    segments[-1].forward(10)
    screen.update()
    time.sleep(0.1)

# Run
screen.mainloop()
