class City:

    def __init__(self, id_city, x_value, y_value):
        self.id_city = id_city
        self.x = x_value
        self.y = y_value

    def write_city_values(self):
        print("[" + str(self.id_city) +"],")
