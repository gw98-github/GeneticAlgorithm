from Idividual import Individual


class RandomAlgorithm:
    def __init__(self, loader):
        self.best_individual = Individual(loader)
        self.loader = loader

    def calculate_random_best_individual(self, number):
        for _ in range(number):
            temp_individual = Individual(self.loader)
            if temp_individual.calculate_travel_length() < self.best_individual.calculate_travel_length():
                self.best_individual = temp_individual
        return self.best_individual
