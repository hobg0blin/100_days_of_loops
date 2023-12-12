import random
from math import sqrt
import time
from svg_turtle import SvgTurtle
turtle = SvgTurtle(1000, 700)
turtle.hideturtle()
# basic geometry help from https://stackoverflow.com/questions/35925378/python-turtle-diagonal-lines-wrong-length

WIDTH = 700
LEN = 700

X = WIDTH * -1
Y = LEN * -1

while Y < LEN:
    turtle.setposition(X, Y)
    if (X < WIDTH):
        rand = random.random()
        angle = 135
        if (rand < 0.5):
            angle = -135
        turtle.left(angle)
        turtle.pendown()
        turtle.forward((WIDTH/100)*sqrt(2))
        turtle.penup()
        X += WIDTH/100 
    else:
        Y += LEN/100
        X = WIDTH * -1

turtle.save_as('maze.svg')

