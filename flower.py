"""
Using Turtle library, given a flower radius
and its amount of petals, draw such flower
in the screen
"""
#!/usr/bin/env python3
from turtle import Turtle, Screen

def draw_petal(turtle:Turtle, radius:int|float):
    """
    A function to draw a petal for a flower of certain radius

    Args:
        turtle (Turtle): The instantiated Turtle object (pen)
        radius (int | float): The radius of the flower
    """
    heading = turtle.heading()
    turtle.begin_fill()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.color("yellow") #To set the fill color for petals
    turtle.end_fill()
    turtle.setheading(heading)

if __name__ == '__main__':
    #To draw a sunflower
    FLOWER_RADIUS = 400 
    AMOUNT_OF_PETALS = 35

    pen = Turtle()
    pen.speed(10)


    for _ in range(AMOUNT_OF_PETALS):
        pen.color("black") #To set the outline color for petals
        draw_petal(pen, FLOWER_RADIUS)
        pen.left(360 / AMOUNT_OF_PETALS)

    pen.hideturtle()

    SCREEN = Screen()
    SCREEN.exitonclick()

