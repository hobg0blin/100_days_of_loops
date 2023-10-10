from pyaxidraw import axidraw
import random
ad = axidraw.AxiDraw()
ad.interactive()
if not ad.connect():            # Open serial port to AxiDraw;
    quit()                      #   Exit, if no connection.
ad.moveto(0, 0)                 # Return Home
ad.moveto(1, 1)                 # Pen-up move to (1, 1) inch
ad.options.units = 1            # Switch to cm units
ad.update()                     # Process changes to options Make a list of points to draw a square, 1 cm on a side: for i in range(30): size = random.randrange(1, 5)
for i in range(30):
    new_points = []
    for p in range(5, 10):
        for q in range(4, 10):
            rand2 = random.randrange(1, 20)
            rand1 = random.randrange(1, 20)
            new_points.append([rand1, rand2])
    print('points: ', new_points)
    ad.draw_path(new_points)            # Plot the path
    ad.moveto(0, 0)                 # Return Home
ad.disconnect()                 # Close serial port

