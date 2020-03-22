import random
from Idividual import Individual

class Mutation:
    def __init__(self, probability):
        self.probability = probability


    def mutate(self, individual):
        for i in range(0, len(individual.individual_cities_array)-1):
            random_number = random.random()
            if random_number<self.probability:
                swap_random = random.randint(0, len(individual.individual_cities_array)-1)
                while swap_random==i:
                    swap_random = random.randint(0, len(individual.individual_cities_array)-1)
                temp_city = individual.individual_cities_array[i]
                individual.individual_cities_array[i] = individual.individual_cities_array[swap_random]
                individual.individual_cities_array[swap_random] = temp_city
        return individual

    def get_result(self):
        return self.individual
