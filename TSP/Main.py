from City import City
from Loader import Loader
from Idividual import Individual
from GreedyAlgorithm import GreedyAlgorithm
from Population import Population
from RandomAlgorithm import RandomAlgorithm
from Mutation import Mutation
from OrderedCrossover import OrderedCrossover
from TournamentSelection import Selection
from GenericAlgorithm import GenericAlgorithm

l1 = Loader('fl417.tsp')

g1 = GenericAlgorithm( 1500,1500, 0.7,0.03,20, l1,"wynik1.xlsx")
g1.calculate()
#g2 = GenericAlgorithm( 1000,100, 0.75,0.03,20, l1,"wynik2.xlsx")
#g2.calculate()
#g3 = GenericAlgorithm( 1000,100, 0.8,0.03,20, l1,"wynik3.xlsx")
#g3.calculate()
#g4 = GenericAlgorithm( 1000,100, 0.85,0.03,20, l1,"wynik4.xlsx")
#g4.calculate()
#g5 = GenericAlgorithm( 1000,100, 0.9,0.03,20, l1,"wynik5.xlsx")
#g5.calculate()

#i1 = Individual(l1)
#i2 = Individual(l1)
#print(i1.write_city_values())
#print(i2.write_city_values())
#oc1 = OrderedCrossover(i1, i2, l1)
#i3 = oc1.get_result()
#print(i3.write_city_values())

#p1 = Population(10000, l1)
#p1.create_random_population()

#s1 = Selection(p1, 100)
#print(s1.selection_result().write_city_values())

#for i in p1.population_array:
#    print(i.write_city_values())

#i1 = Mutation(i1, 0.1, l1).get_result()
#print(i1.write_city_values())

# print("Algorytm zachłanny\n")
# ga1 = GreedyAlgorithm(l1)
# i1.individual_cities_array = ga1.calculate_shortest_travel_combination()
# i1.write_city_values()
# print("Dlugosc trasy to " + "%.2f" % i1.calculate_travel_length() + "\n")
#
# print("Algorytm losowy\n")
# r1 = RandomAlgorithm(l1).calculate_random_best_individual(10000)
# i1.write_city_values()
# print("Dlugosc trasy to " + "%.2f" % r1.calculate_travel_length() + "\n")
