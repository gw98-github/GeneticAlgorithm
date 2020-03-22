import copy
import math
import random
from City import City


class Individual:
    def __init__(self, loader, individual=None):
        self.individual_cities_array = create_random_individual(loader)
        if individual is not None:
            self.individual_cities_array = individual.individual_cities_array


    def write_city_values(self):
        result = ""
        for c in self.individual_cities_array:
            result = result + "[" + str(c.id_city) + "]"
        return result + " value: " + str(self.calculate_travel_length())

    def calculate_travel_length(self):
        travel_length = 0
        for i in range(len(self.individual_cities_array) - 1):
            city1 = self.individual_cities_array[i]
            city2 = self.individual_cities_array[i + 1]
            x_difference_squared = (city1.x - city2.x) ** 2
            y_difference_squared = (city1.y - city2.y) ** 2
            distance = math.sqrt(x_difference_squared + y_difference_squared)
            travel_length += distance
        travel_length += math.sqrt((self.individual_cities_array[0].x - self.individual_cities_array[len(self.individual_cities_array) - 1].x) ** 2 + (self.individual_cities_array[0].y - self.individual_cities_array[len(self.individual_cities_array) - 1].y) ** 2)
        return travel_length


def create_random_individual(loader):
    array = random.sample(loader.cities_array, loader.get_length())
    return array
