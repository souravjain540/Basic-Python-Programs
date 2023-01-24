from turtle import Turtle
from random import randint

aman=Turtle()
aman.color('blue')
aman.shape('turtle')
aman.penup()
aman.goto(-180,100)
aman.pendown()

swati=Turtle()
swati.color('red')
swati.shape('turtle')
swati.penup()
swati.goto(-180,70)
swati.pendown()

ram=Turtle()
ram.color('green')
ram.shape('turtle')
ram.penup()
ram.goto(-180,40)
ram.pendown()

krishna=Turtle()
krishna.color('dark blue')
krishna.shape('turtle')
krishna.penup()
krishna.goto(-180,10)
krishna.pendown()

for movement in range(100):
    aman.forward(randint(1,5))
    swati.forward(randint(1, 5))
    ram.forward(randint(1, 5))
    krishna.forward(randint(1, 5))
if aman.position() > (swati.position() and ram.position()and krishna.position()):
    print(("Aman won the race"))
elif swati.position()>(aman.position() and ram.position() and krishna.position()):
    print("swati won the race")
elif ram.position()> (aman.position() and swati.position() and krishna.position()):
    print("ram won the race")
else:
    print("Krishna won the race")



input(" ...")
