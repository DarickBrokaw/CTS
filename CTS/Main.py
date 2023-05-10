import data_processing
import cp_modeling
import ga_modeling
import schedule_output

# Read in input data and process it
try:
    therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data("input_data.csv"))
except Exception as e:
    print("Error: Failed to process input data.")
    print(e)
    exit()

# Find shared availability between therapists and children
shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)

# Solve using constraint programming model
cp_model = cp_modeling.create_cp_model(shared_availability)
try:
    cp_schedule = cp_modeling.solve_cp_model(cp_model, shared_availability)
except Exception as e:
    print("Error: Failed to solve using constraint programming model.")
    print(e)
    exit()

# Solve using genetic algorithm model
ga_model = ga_modeling.create_ga_model(shared_availability)
try:
    ga_schedule = ga_modeling.solve_ga_model(ga_model, shared_availability)
except Exception as e:
    print("Error: Failed to solve using genetic algorithm model.")
    print(e)
    exit()

# Display and export schedules
schedule_output.display_schedule(cp_schedule)
schedule_output.export_schedule(cp_schedule, "cp_schedule.csv")
schedule_output.display_schedule(ga_schedule)
schedule_output.export_schedule(ga_schedule, "ga_schedule.csv")

