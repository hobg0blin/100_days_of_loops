import math, random
import argparse
from svg_turtle import SvgTurtle
DRAW_FRACTAL = 1 # Set to 1 through 11 and run the program.
turtle = SvgTurtle(800, 800)
parser = argparse.ArgumentParser()
parser.add_argument('fractal')
args = parser.parse_args() 
if (args.fractal):
    print("Drawing fractal: ", args.fractal)
    DRAW_FRACTAL = int(args.fractal)

def drawFilledSquare(size, depth):
    size = int(size)
# Move to the top-right corner before drawing:
    turtle.penup()
    turtle.forward(size // 2)
    turtle.left(90)
    turtle.forward(size // 2)
    turtle.left(180)
    turtle.pendown()
# Alternate between white and gray (with black border):
    if depth % 2 == 0:
        turtle.pencolor('black')
        turtle.fillcolor('white')
    else:
        turtle.pencolor('black')
        turtle.fillcolor('gray')
# Draw a square:
    # SWITCHED TO LINE DRAWING INSTEAD OF FILL
    #########    turtle.begin_fill()
    turtle.pendown()
    for i in range(4): # Draw four lines.
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()
#    turtle.end_fill()
def drawTriangleOutline(size, depth):
    size = int(size)
# Move the turtle to the top of the equilateral triangle:
    height = size * math.sqrt(3) / 2
    turtle.penup()
    turtle.left(90) # Turn to face upward.
    turtle.forward(height * (2/3)) # Move to the top corner.
    turtle.right(150) # Turn to face the bottom-right corner.
    turtle.pendown()
# Draw the three sides of the triangle:
    for i in range(3):
        turtle.forward(size)
        turtle.right(120)

def drawLine(size, depth):
    size = int(size)
# Move the turtle to the top of the equilateral triangle:
    height = size * math.sqrt(3) / 2
    turtle.penup()
    turtle.left(90) # Turn to face upward.
    turtle.forward(height * (2/3)) # Move to the top corner.
    turtle.right(150) # Turn to face the bottom-right corner.
    turtle.pendown()
    turtle.forward(size)

def drawFractal(shapeDrawFunction, size, specs, maxDepth=8, depth=0):
    if depth > maxDepth or size < 1:
        return # BASE CASE
# Save the position and heading at the start of this function call:
    initialX = turtle.xcor()
    initialY = turtle.ycor()
    initialHeading = turtle.heading()
    # Call the draw function to draw the shape:
    turtle.pendown()
    shapeDrawFunction(size, depth)
    turtle.penup()
# RECURSIVE CASE
    for spec in specs:
# Each dictionary in specs has keys 'sizeChange', 'xChange',
# 'yChange', and 'angleChange'. The size, x, and y changes
# are multiplied by the size parameter. The x change and y
# change are added to the turtle's current position. The angle
# change is added to the turtle's current heading.
        sizeCh = spec.get('sizeChange', 1.0)
        xCh = spec.get('xChange', 0.0) *random.randrange(-1, 10)
        # ADDED RANDOMNESS
        # ADDED TANGENT AS WELL
        yCh = spec.get('yChange', 0.0)  *random.randrange(-5, 5)
        angleCh = spec.get('angleChange', 0.0) * random.randrange(1, 10)
# Reset the turtle to the shape's starting point:
        turtle.goto(initialX, initialY)
        turtle.setheading(initialHeading + angleCh)
        turtle.forward(size * xCh)
        turtle.left(90)
        turtle.forward(size * yCh)
        turtle.right(90)
# Make the recursive call:
        drawFractal(shapeDrawFunction, size * sizeCh, specs, maxDepth,
        depth + 1)
if DRAW_FRACTAL == 1:
# Four Corners:
    drawFractal(drawFilledSquare, 150,
    [{'sizeChange': 0.5, 'xChange': -0.5, 'yChange': 0.5},
    {'sizeChange': 0.5, 'xChange': 0.5, 'yChange': 0.5},
    {'sizeChange': 0.5, 'xChange': -0.5, 'yChange': -0.5},
    {'sizeChange': 0.5, 'xChange': 0.5, 'yChange': -0.5}], 5)
elif DRAW_FRACTAL == 2:
# Spiral Squares:
    drawFractal(drawFilledSquare, 600, [{'sizeChange': 0.95,
'angleChange': 7}], 50)
elif DRAW_FRACTAL == 3:
# Double Spiral Squares:
    # experiments: randomness and line instead of fill interesting, recursion depth of 15 seems to last too long
    drawFractal(drawFilledSquare, 600,
    [{'sizeChange': 0.8, 'yChange': 0.05, 'angleChange': -10},
    {'sizeChange': 0.8, 'yChange': -0.05, 'angleChange': 10}], 6)
elif DRAW_FRACTAL == 4:
# Triangle Spiral:
    drawFractal(drawTriangleOutline, 20,
    [{'sizeChange': 1.05, 'angleChange': 7}], 80)
elif DRAW_FRACTAL == 5:
# Conway's Game of Life Glider:
    third = 1 / 3
    drawFractal(drawFilledSquare, 600,
    [{'sizeChange': third, 'yChange': third},
    {'sizeChange': third, 'xChange': third},
    {'sizeChange': third, 'xChange': third, 'yChange': -third},
    {'sizeChange': third, 'yChange': -third},
    {'sizeChange': third, 'xChange': -third, 'yChange': -third}])
elif DRAW_FRACTAL == 6:
# Sierpiński Triangle:
    toMid = math.sqrt(3) / 6
    drawFractal(drawTriangleOutline, 600,
    [{'sizeChange': 0.5, 'yChange': toMid, 'angleChange': 0},
    {'sizeChange': 0.5, 'yChange': toMid, 'angleChange': 120},
    {'sizeChange': 0.5, 'yChange': toMid, 'angleChange': 240}])
elif DRAW_FRACTAL == 7:
# Wave:
    drawFractal(drawTriangleOutline, 280,
    [{'sizeChange': 0.5, 'xChange': -0.5, 'yChange': 0.5},
    {'sizeChange': 0.3, 'xChange': 0.5, 'yChange': 0.5},
    {'sizeChange': 0.5, 'yChange': -0.7, 'angleChange': 15}])
elif DRAW_FRACTAL == 8:
# Horn:
    drawFractal(drawLine, 1,
                [{'sizeChange': 1.02, 'angleChange': 1}], 500)
elif DRAW_FRACTAL == 9:
# Snowflake:
    drawFractal(drawTriangleOutline, 200,
    [{'xChange': math.cos(0 * math.pi / 180),
    'yChange': math.sin(0 * math.pi / 180), 'sizeChange': 0.4},
    {'xChange': math.cos(72 * math.pi / 180),
    'yChange': math.sin(72 * math.pi / 180), 'sizeChange': 0.4},
    {'xChange': math.cos(144 * math.pi / 180),
    'yChange': math.sin(144 * math.pi / 180), 'sizeChange': 0.4},
    {'xChange': math.cos(216 * math.pi / 180),
    'yChange': math.sin(216 * math.pi / 180), 'sizeChange': 0.4},
    {'xChange': math.cos(288 * math.pi / 180),
    'yChange': math.sin(288 * math.pi / 180), 'sizeChange': 0.4}])
elif DRAW_FRACTAL == 10:
# The filled square shape:
    turtle.tracer(1, 0)
    drawFilledSquare(400, 0)
elif DRAW_FRACTAL == 11:
# The triangle outline shape:
    turtle.tracer(1, 0)
    drawTriangleOutline(400, 0)
else:
    assert False, 'Set DRAW_FRACTAL to a number from 1 to 11.'

turtle.save_as(f'fractal_{DRAW_FRACTAL}.svg') # Click the window to exit.
