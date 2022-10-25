'''
Purpose: Draw a polygon to the user's specifications.
Author: VladinXXV
Date: October 23, 2022
'''

#Imports
import turtle as art

#Function definitions
def polygon(sideSize, sideCount, tortoise, color, fill, fillColor = 'black', width = 3):
    '''Draws a polygon of the given specifications.

    Parameters:
        sideSize: the size of each side of the polygon
        sideCount: how many sides the polygon has
        tortoise: a Turtle object that will draw the polygon
        color: the color to draw the polygon in
        fill: whether or not to fill the polygon
        fillColor: the color to fill the polygon with (default black)
        width: how thick the pen should be (default 3)
    '''

    #Tortoise formatting
    tortoise.pencolor(color)
    tortoise.fillcolor(fillColor)
    tortoise.width(width)

    #Start fill
    if fill:
        tortoise.begin_fill()
    
    #Draw the polygon
    for side in range(sideCount):
        tortoise.forward(sideSize)
        tortoise.left(360/sideCount)

    #End fill
    if fill:
        tortoise.end_fill()

def prompt(tortoise):
    '''Prompt user for parameters to draw a polygon with, then draw it.

    Parameters:
        tortoise: a turtle object to draw the polygon with.
    '''

    #Short explanation
    print('This program draws a polygon! Please give me: ')

    #Easy prompts
    sideSize = int(input('Side length: '))
    sideCount = int(input('How many sides: '))
    color = input('Outline color: ')

    #Prompt for fill
    fillCheck = input('Should we fill the polygon? Y/N: ')
    if fillCheck == 'Y' or fillCheck == 'y':
        fill = True
    elif fillCheck == 'N' or fillCheck == 'n':
        fill = False
    else:
        fill = True #Default to True

    #Check if we're filling
    if fill: #If so, ask for fill color and draw
        fillColor = input('Fill color: ')
        polygon(sideSize, sideCount, tortoise, color, fill, fillColor)
    else: #If not, ask for thickness and draw
        width = int(input('Side thickness: '))
        polygon(sideSize, sideCount, tortoise, color, fill, width = width)

def main():
    '''Create a turtle, prompt for polygon, and draw it. Exit on click.
    '''

    #Create the artist
    artist = art.Turtle()
    artist.hideturtle()
    artist.speed(6)

    #Prompt and draw
    prompt(artist)

    #Wait for a click to exit
    canvas = artist.getscreen()
    canvas.exitonclick()

#Call to main
main()
