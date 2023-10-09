import random
import time
import cowsay
from wonderwords import RandomWord


# from collections import namedtuple
from rich.live import Live
from rich.table import Table

char_names = cowsay.char_names
remove = ['stegosaurus', 'turtle', 'trex', 'miki', 'dragon']
animals = [char for char in char_names if char not in remove]

class Project:
    def __init__(self,row_id, project_type, time):
        self.id = row_id
        self.type = project_type
        self.time = time

def snake(sentence, iter_times):
    if (iter_times > 0):
        sentence += ", eating its own mouth, eating its own tail"
        return snake(sentence, iter_times -1)
    else:
        return sentence

def generate_table(iters):
    """Make a new table."""""
    table = Table()
    table.add_column("Let me explain it to you: ")
    table.add_row(cowsay.get_output_string('cow', snake('a snake', iters)))


    return table




animal = random.choice(animals)
with Live(generate_table(0), refresh_per_second=4) as live:
    for _ in range(1, 10000):
        time.sleep(1.5)
        live.update(generate_table(_))
