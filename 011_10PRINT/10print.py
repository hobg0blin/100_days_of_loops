import random
import time
while True:
    rand = random.random()
    val = '\u2571' if rand < 0.5 else '\u2572'
    print(val, end="")
    time.sleep(0.0000000000000000000001)
