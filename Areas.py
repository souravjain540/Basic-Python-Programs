# Program to calculate the areas of 2d shapes

import math

def square(side):
    area = side * side
    return area

def rectangle(length, breadth):
    area = length * breadth
    return area

def triangle(side1, side2, side3):
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area

def circle(radius):
    area = 3.14 * radius * radius
    return area

final_area = 0.0
print("Choose the shape you want to calculate area of: ")

while True:
    print("Square, Rectangle, Triangle, Circle")
    shape = input('>> ')
    print(shape.lower())

    if shape.lower() == "square":
        side = float(input("Enter the value of side: "))
        final_area = square(side)
        break

    elif shape.lower() == "rectangle":
        length = float(input("Enter value of length: "))
        breadth = float(input("Enter value of breadth: "))
        final_area = rectangle(length, breadth)
        break

    elif shape.lower() == "triangle":
        side1 = float(input("Enter the value of 1st side: "))
        side2 = float(input("Enter the value of 2nd side: "))
        side3 = float(input("Enter the value of 3rd side: "))
        final_area = triangle(side1, side2, side3)
        break

    elif shape.lower() == "circle":
        radius = float(input("Enter the value of radius: "))
        final_area = circle(radius)
        break

    else:
        print("Please choose a shape from the given 4 or check your spelling again")

print(f"The area of the shape is: {final_area}")