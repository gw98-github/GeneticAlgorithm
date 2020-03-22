import math
from Loader import Loader


class GreedyAlgorithm:

    def __init__(self, loader):
        self.loader_cities_array = loader.cities_array

    def calculate_shortest_travel_combination(self):
        for i in range(0, len(self.loader_cities_array)-1):
            best_distance = -1
            best_city_position = -1
            for j in range(i+1, len(self.loader_cities_array)):
                actual_distance = calculate_difference(self.loader_cities_array[i], self.loader_cities_array[j])

                if best_distance == -1:
                    best_distance = actual_distance
                    best_city_position = j

                if best_distance > actual_distance:
                    best_distance = actual_distance
                    best_city_position = j

            temp_city = self.loader_cities_array[best_city_position]
            self.loader_cities_array[best_city_position] = self.loader_cities_array[i+1]
            self.loader_cities_array[i + 1] = temp_city


        return self.loader_cities_array


def calculate_difference(city1, city2):
    x_difference_squared = (city1.x - city2.x) ** 2
    y_difference_squared = (city1.y - city2.y) ** 2
    return math.sqrt(x_difference_squared + y_difference_squared)
