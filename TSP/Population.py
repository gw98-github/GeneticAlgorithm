from Idividual import Individual


class Population:
    def __init__(self, size, loader):
        self.loader = loader
        self.size = size
        self.population_array = []
        self.create_random_population()

    def create_random_population(self):
        for i in range(0, self.size):
            self.population_array.append(Individual(self.loader))
