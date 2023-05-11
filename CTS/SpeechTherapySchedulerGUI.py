import tkinter as tk
from tkinter import filedialog, messagebox
from tabulate import tabulate
import CP_Modeling
import GA_Modeling
import Schedule_Output
import Data_Processing
import SpeechTherapySchedulerGUI
import Main


class SpeechTherapySchedulerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speech Therapy Scheduler")

        # create widgets
        self.input_label = tk.Label(self.root, text="Input File:")
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_button = tk.Button(self.root, text="Browse", command=self.browse_input_file)
        self.cp_button = tk.Button(self.root, text="Solve Using Constraint Programming", command=self.solve_cp_model)
        self.ga_button = tk.Button(self.root, text="Solve Using Genetic Algorithm", command=self.solve_ga_model)
        self.cp_label = tk.Label(self.root, text="Constraint Programming Schedule:")
        self.cp_text = tk.Text(self.root, width=80, height=10)
        self.ga_label = tk.Label(self.root, text="Genetic Algorithm Schedule:")
        self.ga_text = tk.Text(self.root, width=80, height=10)
        self.export_button = tk.Button(self.root, text="Export Schedule", command=self.export_schedule)

        # layout widgets
        self.input_label.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)
        self.input_button.grid(row=0, column=2)
        self.cp_button.grid(row=1, column=0, columnspan=3, pady=10)
        self.cp_label.grid(row=2, column=0, columnspan=3)
        self.cp_text.grid(row=3, column=0, columnspan=3, padx=10)
        self.ga_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.ga_label.grid(row=5, column=0, columnspan=3)
        self.ga_text.grid(row=6, column=0, columnspan=3, padx=10)
        self.export_button.grid(row=7, column=0, columnspan=3, pady=10)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, file_path)

    def solve_cp_model(self):
        input_file = self.input_entry.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data(input_file))
        except Exception as e:
            messagebox.showerror("Error", "Failed to process input data.\n" + str(e))
            return
        shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)
        cp_model = cp_modeling.create_cp_model(shared_availability)
        try:
            cp_schedule = cp_modeling.solve_cp_model(cp_model, shared_availability)
        except Exception as e:
            messagebox.showerror("Error", "Failed to solve using constraint programming model.\n" + str(e))
            return
        self.cp_text.delete("1.0", tk.END)
        self.cp_text.insert("1.0", tabulate(cp_schedule, headers='keys', tablefmt='fancy_grid'))

    def solve_ga_model(self):
        input_file = self.input_entry.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data(input_file))
        except Exception as e:
            messagebox.showerror("Error", "Failed to process input data.\n" + str(e))
            return
        shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)
        ga_model = ga_modeling.create_ga_model(shared_availability)
        try:
            ga_schedule = ga_modeling.solve_ga_model(ga_model, shared_availability)
        except Exception as e:
            messagebox.showerror("Error", "Failed to solve using genetic algorithm model.\n" + str(e))
            return
        self.ga_text.delete("1.0", tk.END)
        self.ga_text.insert("1.0", tabulate(ga_schedule, headers='keys', tablefmt='fancy_grid'))

    def browse_input_file(self):
        file_path = filedialog.askopenfilename()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, file_path)

    def solve_cp_model(self):
        input_file = self.input_entry.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data(input_file))
        except Exception as e:
            messagebox.showerror("Error", "Failed to process input data.\n" + str(e))
            return
        shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)
        cp_model = cp_modeling.create_cp_model(shared_availability)
        try:
            cp_schedule = cp_modeling.solve_cp_model(cp_model, shared_availability)
        except Exception as e:
            messagebox.showerror("Error", "Failed to solve using constraint programming model.\n" + str(e))
            return
        self.cp_text.delete("1.0", tk.END)
        self.cp_text.insert("1.0", tabulate(cp_schedule, headers='keys', tablefmt='fancy_grid'))

    def solve_ga_model(self):
        input_file = self.input_entry.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data(input_file))
        except Exception as e:
            messagebox.showerror("Error", "Failed to process input data.\n" + str(e))
            return
        shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)
        ga_model = ga_modeling.create_ga_model(shared_availability)
        try:
            ga_schedule = ga_modeling.solve_ga_model(ga_model, shared_availability)
        except Exception as e:
            messagebox.showerror("Error", "Failed to solve using genetic algorithm model.\n" + str(e))
            return
        self.ga_text.delete("1.0", tk.END)
        self.ga_text.insert("1.0", tabulate(ga_schedule, headers='keys', tablefmt='fancy_grid'))

    def export_schedule(self):
        input_file = self.input_entry.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            therapist_availability, children_availability = data_processing.process_input_data(data_processing.read_input_data(input_file))
        except Exception as e:
            messagebox.showerror("Error", "Failed to process input data.\n" + str(e))
            return
        shared_availability = data_processing.find_shared_availability(therapist_availability, children_availability)
        if not shared_availability:
            messagebox.showwarning("Warning", "No shared availability found.")
            return
        if not cp_model:
            messagebox.showwarning("Warning", "Constraint programming model not yet solved.")
            return
        if not ga_model:
            messagebox.showwarning("Warning", "Genetic algorithm model not yet solved.")
            return
        try:
            schedule_output.export_schedule(therapist_availability, children_availability, cp_model, ga_model)
        except Exception as e:
            messagebox.showerror("Error", "Failed to export schedule.\n" + str(e))
            return

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    scheduler_gui = SpeechTherapySchedulerGUI()
    scheduler_gui.run()