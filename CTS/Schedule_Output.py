import pandas as pd
from tabulate import tabulate
import CP_Modeling
import GA_Modeling
import Schedule_Output
import Data_Processing
import SpeechTherapySchedulerGUI
import Main

def display_schedule(schedule):
    print(tabulate(schedule, headers='keys', tablefmt='fancy_grid'))

def export_schedule(schedule, filename):
    schedule.to_csv(filename, index=False)

