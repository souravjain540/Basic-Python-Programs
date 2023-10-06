import turtle
import datetime

# Creates Initial Screen
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("white")

# Draw the clock face
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.penup()
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.circle(200)

# Make custom shape for clock hands - Currently Lines
turtle.register_shape("hour_hand", ((-4, -5), (4, -5), (2, 150), (-2, 150)))
turtle.register_shape("minute_hand", ((-2, -5), (2, -5), (1, 200), (-1, 200)))
turtle.register_shape("second_hand", ((-1, -5), (1, -5), (0.5, 220), (-0.5, 220)))

# Creating clock hands
hands = []
for shape, color in [("hour_hand", "black"), ("minute_hand", "blue"), ("second_hand", "red")]:
    hand = turtle.Turtle()
    hand.shape(shape)
    hand.color(color)
    hands.append(hand)

# Function to update position of clock hands
def update_clock_hands():
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Considers current time (hour, minute, and second) to  calculate position
    angles = [
        (hour + minute / 60) * 360 / 12,
        (minute + second / 60) * 360 / 60,
        (second + now.microsecond / 1000000) * 360 / 60
    ]

    # Align the clock hands on the clock face by converting the clock angles to turtle angles.
    for hand, angle in zip(hands, angles):
        hand.setheading(90 - angle)

# Create a digital time display over clock
digital_time_display = turtle.Turtle()
digital_time_display.speed(0)
digital_time_display.penup()
digital_time_display.goto(0, 250)
digital_time_display.pendown()
digital_time_display.hideturtle()

# Function to update digital time based on - gets current time, clears previous screen, write new time 
def update_digital_time():
    now = datetime.datetime.now()
    digital_time_display.clear()
    digital_time_display.write(now.strftime("%H:%M:%S"), align="center", font=("Arial", 24, "normal"))

# A timer to update screen to update clock and digital time
def update_clock():
    update_clock_hands()
    update_digital_time()
    screen.update()
    screen.ontimer(update_clock, 1000)

# Keep updating the clock
update_clock()

# Close the turtle graphics window on click
screen.exitonclick()
turtle.bye()
