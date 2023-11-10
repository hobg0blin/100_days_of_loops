import time
from rich.text import Text
from rich.live import Live
from rich.table import Table



def generate_table():
    """Make a new table."""""
    table = Table(width=35, show_lines=True)
    text = Text("Repeated, consistent actions make us who we are. This is not to say we cannot change - there is almost always an escape case - but that the loop is the pattern that makes the person.")
    table.add_column("Loops define us.")
    table.add_row(text)
    return table



with Live(generate_table(), refresh_per_second=4) as live:
    for i in range(0, 10000):
        time.sleep(0.5)
        live.update(generate_table())


