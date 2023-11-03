import random
import time
from rich.live import Live
from rich.table import Table


WIDTH = 51  # Width of the maze (must be odd).
HEIGHT = 25  # Height of the maze (must be odd).
assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3
SEED = 1
random.seed(SEED)

# Use these characters for displaying the maze:
EMPTY = ' '
MARK = '@'
WALL = chr(9608)  # Character 9608 is '█'
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e', 'w'

# Create the filled-in maze data structure to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL  # Every space is a wall at first.

def generate_table(maze, coord=0):
    """Make a new table."""""
#    print('player coords: ', hasVisited[coord][0])
    table = Table()
    table.add_column('A MAZE')
    table.add_row(printMaze(maze, hasVisited[coord][0], hasVisited[coord][1]))
    return table

def printMaze(maze, markX=None, markY=None):
    """Displays the maze data structure in the maze argument. The
    markX and markY arguments are coordinates of the current
    '@' location of the algorithm as it generates the maze."""
    out = ''
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                # Display the '@' mark here:
                out += MARK
            else:
                # Display the wall or empty space:
                out += maze[(x, y)]
        out += "\n"  # Print a newline after printing the row.
    return out

def visit(x, y):
    """"Carve out" empty spaces in the maze at x, y and then
    recursively move to neighboring unvisited spaces. This
    function backtracks when the mark has reached a dead end."""
    maze[(x, y)] = EMPTY  # "Carve out" the space at x, y.
    #printMaze(maze, x, y)  # Display the maze as we generate it.
    #print('\n\n')

    while True:
        # Check which neighboring spaces adjacent to
        # the mark have not been visited already:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)

        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)

        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)

        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            # BASE CASE
            # All neighboring spaces have been visited, so this is a
            # dead end. Backtrack to an earlier space:
            return
        else:
            # RECURSIVE CASE
            # Randomly pick an unvisited neighbor to visit:
            nextIntersection = random.choice(unvisitedNeighbors)

            # Move the mark to an unvisited neighboring space:

            if nextIntersection == NORTH:
                nextX = x
                nextY = y - 2
                maze[(x, y - 1)] = EMPTY  # Connecting hallway.
            elif nextIntersection == SOUTH:
                nextX = x
                nextY = y + 2
                maze[(x, y + 1)] = EMPTY  # Connecting hallway.
            elif nextIntersection == WEST:
                nextX = x - 2
                nextY = y
                maze[(x - 1, y)] = EMPTY  # Connecting hallway.
            elif nextIntersection == EAST:
                nextX = x + 2
                nextY = y
                maze[(x + 1, y)] = EMPTY  # Connecting hallway.

            hasVisited.append((nextX, nextY))  # Mark as visited.
            visit(nextX, nextY)  # Recursively visit this space.


# Carve out the paths in the maze data structure:
hasVisited = [(1, 1)]  # Start by visiting the top left corner.
visit(1, 1)
print('has visited: ', hasVisited)

player_coords = 0
with Live(generate_table(maze, player_coords), refresh_per_second=4) as live:
    for i in range(0, 10000):
        time.sleep(0.5)
        live.update(generate_table(maze, player_coords))
        player_coords += 1
        if player_coords >= len(hasVisited): 
            player_coords = 0


# Display the final resulting maze data structure:

