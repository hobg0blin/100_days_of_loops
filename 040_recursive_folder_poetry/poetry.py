import os
import shutil
import time
from rich.live import Live
from rich.table import Table

poem = ["the noise is drowning the signal", "there is too much to be afraid of"]
poem_path = "./words"
if os.path.exists(poem_path) and os.path.isdir(poem_path):
    shutil.rmtree(poem_path)
os.mkdir(poem_path)

def list_files(startpath):
    output_string = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_string += ('{}{}'.format(indent, os.path.basename(root)) + "\n")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_string += ('{}{}'.format(subindent, f) + "\n")
    return output_string


def generate_table():
    """Make a new table."""""
    table = Table()
    files = list_files(poem_path)
    if len(files) > 1:
        title = files.split()[0]
        table.add_column(files.split()[0])
        table.add_row(files.replace(title,""))
    else:
        table.add_column('wait')
        table.add_row("Writing...")
    return table


def add_words(dir, words, live):
    if len(words) <= 0:
        return
    else:
        path = os.path.join(dir, words[0])
        os.mkdir(path)
        time.sleep(1.5)
        live.update(generate_table())
        add_words(path, words[1:], live)



with Live(generate_table(), refresh_per_second=4) as live:
    for line in poem:
        add_words(poem_path, line.split(), live)
            
        
