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
poisons = ['aversion to', 'ignorance of', 'attachment to']
r = RandomWord()

class Project:
    def __init__(self,row_id, project_type, time):
        self.id = row_id
        self.type = project_type
        self.time = time


def generate_table(stage, new_animal):
    """Make a new table."""""
    table = Table()
    if (stage == 1):
        table.add_column("You reincarnated as: " + new_animal)
        table.add_row(cowsay.get_output_string(new_animal, random.choice(['hey', 'sup', 'yo'])))

    if (stage == 2):
        poison = poisons[random.randint(0, 2)]
        poison_subject = r.word(include_categories=["noun"])
        table.add_column(f"You developed an {poison} {poison_subject}s")
        table.add_row(cowsay.get_output_string(new_animal, random.choice(['damn', 'oops', 'aw rats'])))

    if (stage == 3):
        table.add_column(f"You died!")
        table.add_row(cowsay.get_output_string(new_animal, 'oh no'))

    return table




animal = random.choice(animals)
with Live(generate_table(1, animal), refresh_per_second=4) as live:
    stage = 2
    for _ in range(10000):
        time.sleep(1.5)
        live.update(generate_table(stage, animal))
        if (stage < 3):
            stage += 1
        else:
            animal = random.choice(animals)
            stage = 1
