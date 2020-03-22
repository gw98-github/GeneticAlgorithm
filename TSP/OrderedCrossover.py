import random
from Idividual import Individual


class OrderedCrossover:
    def __init__(self, Px, loader):
        self.loader = loader
        self.Px = Px

    def crossover(self, f_individual, s_individual):
        ran = random.uniform(0,1)
        if ran<self.Px :
            result = [None] * (len(f_individual.individual_cities_array))

            random_numbers = random.sample(range(0, len(f_individual.individual_cities_array) - 1), 2)
            random_numbers.sort()

            for i in range(0, len(f_individual.individual_cities_array)):
                if random_numbers[0] <= i <= random_numbers[1]:
                    result[i] = f_individual.individual_cities_array[i]

            for i in range(0, len(f_individual.individual_cities_array)):
                if result[i] is None:
                    for j in range(0, len(f_individual.individual_cities_array)):
                        if s_individual.individual_cities_array[j] not in result:
                            result[i] = s_individual.individual_cities_array[j]
                            break
            result_individual = Individual(self.loader)
            result_individual.individual_cities_array = result
            return result_individual
        else:
            return f_individual



