import random
import time
from svg_turtle import SvgTurtle
turtle = SvgTurtle(700, 700)
turtle.hideturtle()
def drawBranch(startPosition, direction, branchLength):
    if branchLength < 5:
# BASE CASE
        return
# Go to the starting point & direction.
    turtle.penup()
    turtle.goto(startPosition)
    turtle.setheading(direction)
# Draw the branch (thickness is 1/7 the length).
    if branchLength < 50:
        turtle.pendown()
    turtle.pensize(max(branchLength / 7.0, 1))
    turtle.forward(branchLength)
# Record the position of the branch's end.
    endPosition = turtle.position() * random.randrange(-4, 4)
    leftDirection = direction + random.randint(10, 45)
    leftBranchLength = branchLength - random.randint(7, 15)
    rightDirection = direction - random.randint(10, 45)
    rightBranchLength = branchLength - random.randint(7, 15)
# RECURSIVE CASE
    drawBranch(endPosition, leftDirection, leftBranchLength)
    drawBranch(endPosition, rightDirection, rightBranchLength)
seed = 0
# Get pseudorandom numbers for the branch properties.
random.seed(seed)
LEFT_ANGLE = random.randint(10, 30)
LEFT_DECREASE = random.randint( 8, 15)
RIGHT_ANGLE = random.randint(10, 30)
RIGHT_DECREASE = random.randint( 8, 15)
START_LENGTH = random.randint(100, 130)
# Write out the seed number.
turtle.clear()
turtle.penup()
# turtle.goto(10, 10)
# Draw the tree.
drawBranch((0, -450), 90, START_LENGTH)
drawBranch((0, 600), -90, START_LENGTH)
#    turtle.update()
time.sleep(2)
seed = seed + 1
turtle.save_as('tree.svg')
