import os
import sys
import turtle
from sys import exit
import random
sys.setrecursionlimit(1900)

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1524, height=800)
user_input = screen.textinput(title="Turtle Race", prompt="Who's going to win the race?")


def check_position(*args):
    game_over = 0
    for i in args:
        if i.xcor() >= 750:
            print(f"{i.color()[0]} color turtle wins.")
            game_over = 1
            break
        else:
            pass
    if game_over == 1:
        os.system("pause")
        exit()
    else:
        move_turtles(*args)


def move_turtles(*args):
    for i in args:
        random_steps = random.randint(0, 10)
        i.speed(random_steps)
        i.forward(random_steps)
    check_position(*args)


t1 = turtle.Turtle()
t1.setposition(-762, 0)
t1.penup()
t1.shape("turtle")
t1.color("red")

t2 = turtle.Turtle()
t2.setposition(-762, 0)
t2.shape("turtle")
t2.penup()
t2.sety(25)
t2.color("blue")

t3 = turtle.Turtle()
t3.setposition(-762, 0)
t3.penup()
t3.sety(-25)
t3.shape("turtle")
t3.color("green")

t4 = turtle.Turtle()
t4.setposition(-762, 0)
t4.penup()
t4.sety(-50)
t4.shape("turtle")
t4.color("white")


move_turtles(t1, t2, t3, t4)
screen.mainloop()
