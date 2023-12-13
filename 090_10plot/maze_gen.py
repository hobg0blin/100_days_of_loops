import random
from math import sqrt
import time
from svg_turtle import SvgTurtle
turtle = SvgTurtle(1000, 700)
turtle.hideturtle()
# basic geometry help from https://stackoverflow.com/questions/35925378/python-turtle-diagonal-lines-wrong-length

WIDTH = 700
LEN = 700
SEGMENTS = 50

X = WIDTH * -1
Y = LEN * -1
turtle.penup()
while Y < LEN:
    turtle.setposition(X, Y)
    if (X < WIDTH):
        rand = random.random()
        angle = 135
        if (rand < 0.5):
            angle = -135
        turtle.left(angle)
        turtle.pendown()
        turtle.forward((WIDTH/SEGMENTS)*sqrt(2))
        turtle.penup()
        turtle.right(angle)
        #if (angle < 0):
        #            turtle.forward((WIDTH/SEGMENTS)*sqrt(2))
        X += WIDTH/SEGMENTS 
    else:
        Y += LEN/SEGMENTS
        X = WIDTH * -1

turtle.save_as('maze.svg')

