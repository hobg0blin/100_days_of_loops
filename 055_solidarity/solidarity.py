import os
import shutil
import time
from rich.text import Text
from rich.live import Live
from rich.table import Table



def generate_table(i):
    """Make a new table."""""
    table = Table(width=70, show_lines=True)
    solidarity = Text("SOLIDARITY ")
    solidarity.stylize("bold red")
    for j  in range (0, i):
        table.add_row(solidarity + solidarity + solidarity + solidarity + solidarity)
    return table



with Live(generate_table(1), refresh_per_second=4) as live:
    for i in range(0, 10000):
        time.sleep(0.5)
        live.update(generate_table(i))
            
        
