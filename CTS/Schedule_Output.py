import pandas as pd
from tabulate import tabulate

def display_schedule(schedule):
    print(tabulate(schedule, headers='keys', tablefmt='fancy_grid'))

def export_schedule(schedule, filename):
    schedule.to_csv(filename, index=False)

