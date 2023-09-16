import turtle
from sys import exit


class Tim:
    def __init__(self):
        self.tim = turtle.Turtle()

    def move_front(self):
        self.tim.fd(5)

    def move_back(self):
        self.tim.bk(5)

    def turn_left(self):
        self.tim.lt(90)

    def turn_right(self):
        self.tim.rt(90)

    def cw(self):
        angle = self.tim.heading()
        angle -= 10
        self.tim.setheading(angle)

    def acw(self):
        angle = self.tim.heading()
        angle += 10
        self.tim.setheading(angle)


obj = Tim()
screen = turtle.Screen()
screen.listen()
screen.onkeypress(fun=obj.move_front, key="f")
screen.onkeypress(fun=obj.move_back, key="b")
screen.onkeypress(fun=obj.turn_right, key="r")
screen.onkeypress(fun=obj.turn_left, key="l")
screen.onkeypress(fun=exit, key="e")
screen.onkeypress(fun=screen.reset, key="c")
screen.onkeypress(fun=obj.cw, key="w")
screen.onkeypress(fun=obj.acw, key="a")
screen.mainloop()
