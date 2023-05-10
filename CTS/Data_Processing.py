import pandas as pd

def create_availability_dataframe(user_input):
    data = {
        'Name': [],
        'Day': [],
        'Start': [],
        'End': []
    }
    return pd.DataFrame(data)

def read_input_data(filename):
    # read in input data from a CSV file or other format
    return input_data

def process_input_data(input_data):
    therapist_input = None
    children_input = None

    therapist_availability = create_availability_dataframe(therapist_input)
    children_availability = create_availability_dataframe(children_input)

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

