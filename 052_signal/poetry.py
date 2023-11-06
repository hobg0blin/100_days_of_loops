import os
import shutil
import time
from rich.live import Live
from rich.table import Table

poem = ["something is terribly wrong", "...", "something is terribly wrong", "...", "something is terribly wrong", "..."]
poem_path = "./a faint signal in the background"
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
        print('files: ', files.split())
        title = "a faint signal in the background"
        print('files: ', files)
        print('title: ', title)
        table.add_column(title)
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
        print('path: ', path)
        if os.path.exists(path + "  "):
            path = path + "   "
            print('new path: ', path)
            os.mkdir(path)

        if os.path.exists(path + " "): 
            path = path + "  "
            print('new path: ', path)
            os.mkdir(path)
        elif os.path.exists(path):
            path = path + " "
            print('new path: ', path)
            os.mkdir(path)

        else:
            os.mkdir(path)
        time.sleep(1.5)
        live.update(generate_table())
        add_words(path, words[1:], live)



with Live(generate_table(), refresh_per_second=4) as live:
    for line in poem:
        add_words(poem_path, line.split(), live)
            
        
