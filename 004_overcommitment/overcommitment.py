import random
import time
# from collections import namedtuple
from rich.live import Live
from rich.table import Table

project_types = ["art", "freelance", "open-source", "A/V", "game"]
class Project:
    def __init__(self,row_id, project_type, time):
        self.id = row_id
        self.type = project_type
        self.time = time

projects = []
burnout = False
burnout_days = 0

def generate_table(burnout, burnout_days, value):
    """Make a new table."""""
    table = Table()
    if (burnout):
        table.add_column("You overcommitted!!!")
        table.add_row("[red]YOU ARE BURNED OUT")
        table.add_row(f"[red]DAY {burnout_days}")
    elif (value > 75):
        table.add_column("[red]You fucking idiot!")
        new_project = create_project(len(projects))
        table.add_row(f"You added a new {new_project.type} project that will take {new_project.time} days")
        projects.append(new_project)
        row_id = len(projects)
    else:
        table.add_column("ID")
        table.add_column("Project")
        table.add_column("Status")

        for project in projects:
            project.time -= 1
            if project.time >= 0:
                table.add_row(
                    f"{project.id}", f"{project.type}", f"Days remaining: {project.time}"
                )
            else:
                projects.remove(project)

    return table

def create_project(row_id):
    project = random.choice(project_types)
    time = random.randint(1, 40)
    p = Project(row_id, project, time)
    return p



with Live(generate_table(burnout, burnout_days, 75), refresh_per_second=4) as live:
    live.burnout = burnout
    live.burnout_days = burnout_days
    for _ in range(10000):
        value = random.random() * 100
        if (len(projects) > 5 and value < 35 and burnout == False):
            burnout = True
        elif (burnout == True and value < 25):
            burnout = False
            burnout_days = 0
        if (burnout):
            burnout_days += 1
        # live.console.print('burnout days: ', burnout_days)
        time.sleep(0.75)
        live.update(generate_table(burnout, burnout_days, value))
