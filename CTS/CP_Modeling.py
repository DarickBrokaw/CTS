from ortools.sat.python import cp_model

def create_cp_model(shared_availability):
    model = cp_model.CpModel()
    variables = []
    variable_to_index = {}
    index_to_variable = {}
    for index, row in shared_availability.iterrows():
        var_name = f"{row['Therapist']}_{row['Child']}_{row['Day']}_{row['Start']}"
        var = model.NewBoolVar(var_name)
        variables.append(var)
        variable_to_index[var_name] = index
        index_to_variable[index] = var

    # Each therapist can have only one session per day
    for day in shared_availability['Day'].unique():
        therapists = shared_availability[shared_availability['Day'] == day]['Therapist'].unique()
        for therapist in therapists:
            sessions = []
            for index, row in shared_availability.iterrows():
                if row['Day'] == day and row['Therapist'] == therapist:
                    sessions.append(index_to_variable[index])
            model.Add(sum(sessions) <= 1)

    # Each child can have only one session per day
    for day in shared_availability['Day'].unique():
        children = shared_availability[shared_availability['Day'] == day]['Child'].unique()
        for child in children:
            sessions = []
            for index, row in shared_availability.iterrows():
                if row['Day'] == day and row['Child'] == child:
                    sessions.append(index_to_variable[index])
            model.Add(sum(sessions) <= 1)

    # Sessions involving the same child must be back-to-back
    for day in shared_availability['Day'].unique():
        children = shared_availability[shared_availability['Day'] == day]['Child'].unique()
        for child in children:
            sessions = []
            start_times = []
            for index, row in shared_availability.iterrows():
                if row['Day'] == day and row['Child'] == child:
                    sessions.append(index_to_variable[index])
                    start_times.append(row['Start'])
            num_sessions = len(sessions)
            for i in range(num_sessions - 1):
                if start_times[i+1] - start_times[i] != 1:
                    model.Add(sessions[i+1] == sessions[i])

    # Minimize the total number of sessions
    model.Minimize(sum(variables))

    return model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self._variables = variables
        self._solution_count = 0

    def on_solution_callback(self):
        self._solution_count += 1

    def solution_count(self):
        return self._solution_count

def solve_cp_model(cp_model, shared_availability):
    solver = cp_model.CpSolver()
    variables = []
    solution_printer = SolutionPrinter(variables)
    solver.SearchForAllSolutions(cp_model, solution_printer)

    schedule = []
    for _, row in shared_availability.iterrows():
        var_name = f"{row['Therapist']}_{row['Child']}_{row['Day']}_{row['Start']}"
        if solver.Value(variables[variable_to_index[var_name]]) == 1:
            schedule.append({
                'Therapist': row['Therapist'],
                'Child': row['Child'],
                'Day': row['Day'],
                'Start': row['Start'],
                'End':

