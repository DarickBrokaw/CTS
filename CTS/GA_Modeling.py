from deap import algorithms, base, creator, tools

def create_ga_model(shared_availability):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    def create_individual(shared_availability):
        return [0] * len(shared_availability)

    toolbox = base.Toolbox()
    toolbox.register("individual", create_individual, shared_availability)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def evaluate(individual):
        return sum(individual),

    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox

def solve_ga_model(ga_model, shared_availability):
    pop = ga_model.population(n=50)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    pop, logbook = algorithms.eaSimple(pop, ga_model, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats)

    best_individual = tools.selBest(pop, k=1)[0]
    best_session_indices = [i for i, x in enumerate(best_individual) if x == 1]
    schedule = shared_availability.iloc[best_session_indices]
    return schedule

