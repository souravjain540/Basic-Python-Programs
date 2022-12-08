
import turtle
import math
import random

sierpinski = turtle.Turtle()
sierpinski.width(3)
triangle_side_length = 500
total_number_of_dots = 2000
slope = -(math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2)))/(triangle_side_length/2)

vertex_a = [0, math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]
vertex_b = [triangle_side_length/2, -math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]
vertex_c = [-triangle_side_length/2, -math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]

verticies = [vertex_a, vertex_b, vertex_c]

random_x_coordinate = random.uniform(-triangle_side_length/2, triangle_side_length/2)
random_y_coordinate = random.uniform(
    -math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2,
    (slope * abs(random_x_coordinate)) + math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2
    )
random_point = [random_x_coordinate, random_y_coordinate]

def draw_triangle():
    sierpinski.penup()
    sierpinski.setpos(vertex_a[0], vertex_a[1])
    sierpinski.pendown()
    sierpinski.goto(vertex_b[0], vertex_b[1])
    sierpinski.goto(vertex_c[0], vertex_c[1])
    sierpinski.goto(vertex_a[0], vertex_a[1])
    sierpinski.penup()
    sierpinski.setpos(random_point[0], random_point[1])
    sierpinski.dot()
    dots = 0
    while dots < total_number_of_dots:
        position = random.choice(list(verticies))
        sierpinski.setpos(position[0]-((position[0]-sierpinski.pos()[0])/2), position[1]-((position[1]-sierpinski.pos()[1])/2))
        sierpinski.dot()
        dots+=1

draw_triangle()

turtle.done()
