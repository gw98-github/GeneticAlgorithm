from City import City


class Loader:

    def __init__(self, file_name):
        self.cities_array = get_cities_from_file(file_name)
        self.length = len(get_cities_from_file(file_name))

    def list_all_cities(self):
        for a in self.cities_array:
            a.write_city_values()

    def get_length(self):
        return self.length


def get_cities_from_file(file_name):
    with open('TSP_dane/' + file_name, 'r') as f:
        cities_arr = []
        for _ in range(3):
            next(f)
        x = f.readline().split(": ")
        length = int(x[1])
        next(f)
        next(f)
        for _ in range(length):
            values = f.readline().split(" ")
            city = City(int(values[0]), float(values[1]), float(values[2]))
            cities_arr.append(city)
        return cities_arr
