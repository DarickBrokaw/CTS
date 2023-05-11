import tkinter as tk
from tkinter import filedialog, messagebox
from tabulate import tabulate
import pandas as pd
import CP_Modeling
import GA_Modeling
import Schedule_Output
import Data_Processing
import SpeechTherapySchedulerGUI
import Main

def create_availability_dataframe():
    data = {
        'Name': [],
        'Day': [],
        'Start': [],
        'End': []
    }
    return pd.DataFrame(data)

def read_input_data(filename):
    try:
        input_data = pd.read_csv(filename)
    except Exception as e:
        raise Exception("Failed to read input file: " + str(e))
    return input_data

def process_input_data(input_data):
    therapist_input = input_data[input_data['Type'] == 'therapist'].reset_index(drop=True)
    children_input = input_data[input_data['Type'] == 'child'].reset_index(drop=True)

    therapist_availability = create_availability_dataframe()
    children_availability = create_availability_dataframe()

    for i, row in therapist_input.iterrows():
        name = row['Name']
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            start = row[day + ' Start']
            end = row[day + ' End']
            if pd.notna(start) and pd.notna(end):
                therapist_availability = therapist_availability.append({
                    'Name': name,
                    'Day': day,
                    'Start': start,
                    'End': end
                }, ignore_index=True)

    for i, row in children_input.iterrows():
        name = row['Name']
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            start = row[day + ' Start']
            end = row[day + ' End']
            if pd.notna(start) and pd.notna(end):
                children_availability = children_availability.append({
                    'Name': name,
                    'Day': day,
                    'Start': start,
                    'End': end
                }, ignore_index=True)

    return therapist_availability, children_availability

def find_shared_availability(therapist_availability, children_availability):
    shared_availability = []

    for _, t_avail in therapist_availability.iterrows():
        for _, c_avail in children_availability.iterrows():
            if t_avail["Day"] == c_avail["Day"]:
                start_time = max(t_avail["Start"], c_avail["Start"])
                end_time = min(t_avail["End"], c_avail["End"])
                if start_time < end_time:
                    shared_availability.append({
                        "Therapist": t_avail["Name"],
                        "Child": c_avail["Name"],
                        "Day": t_avail["Day"],
                        "Start": start_time,
                        "End": end_time
                    })

    return pd.DataFrame(shared_availability)