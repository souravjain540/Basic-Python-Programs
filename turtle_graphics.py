import random
import turtle
import colorgram
i = -750
j = -400
dots = 0
pen = turtle.Turtle()
pen.speed("fastest")
turtle.bgcolor("black")
turtle.screensize(800, 800)
screen = turtle.Screen()
screen.colormode(255)
pen.penup()
pen.setposition(i, j)
colors = colorgram.extract("hirst.jpg", 6)
lst = [[color.rgb[i] for i in range(3)]for color in colors]
while dots <= 364:
    random_color = random.choice(lst)
    pen.pendown()
    pen.dot(50, tuple(random_color))
    pen.penup()
    if i in range(-750, 750) and j in range(-400, 400):
        pen.forward(60)
        i += 60
        if i in range(700, 750) and j in range(350, 400):
            break
    else:
        i = -750
        j += 60
        pen.setposition(i, j)
        print(pen.position())

    dots += 1
screen.exitonclick()
screen.mainloop()
