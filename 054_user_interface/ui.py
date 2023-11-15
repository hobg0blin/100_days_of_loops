import os
import shutil
import time
from rich.text import Text
from rich.live import Live
from rich.table import Table



def generate_table():
    """Make a new table."""""
    table = Table(width=70, show_lines=True)
    title = Text("Interfaces are")
    text = Text("When you act upon an interface, it acts upon you. By presenting you with limited choices,")
    text2 = Text("by highlighting certain text", style="bold green")
    table.add_column(title, "a feedback loop")
    table.add_column("a feedback loop")
    table.add_row(text, text2)
    table.add_row("By constraining your choices", "with buttons", style="on green")
    table.add_row("In turn, through years of study, your actions determine how interfaces are designed.", " But every choice made in interface design is, by its nature, one of limitation.")
    table.add_row("It is my contention that the modern user interface robs users of their power. It makes us complacent.", "It distances us from the 'bare metal' of the machines that determine so much of our lives. It makes us dependent on the interface, not the machine.")
    table.add_row("By determining the best way to rob users of their power, interfaces allow their creators to profit while slowly robbing their users of even the knowledge of what is possible.", "I do not believe this to be a desirable circumstance.")
    return table



with Live(generate_table(), refresh_per_second=4) as live:
    for i in range(0, 10000):
        time.sleep(0.5)
        live.update(generate_table())
            
        
