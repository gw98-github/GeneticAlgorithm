import random
from Population import Population
from Idividual import Individual

class Selection:
    def __init__(self, N_param):
        self.N_param = N_param

    def selection_result(self, population):
        selected_part_of_population = []
        random_indexes = random.sample(range(0, len(population.population_array)), self.N_param)
        for i in range(len(population.population_array)):
            if i in random_indexes:
                selected_part_of_population.append(population.population_array[i])
        best = None
        for i in selected_part_of_population:
            if best is None:
                best = i
            else:
                if i.calculate_travel_length()<best.calculate_travel_length():
                    best = i
        return best

