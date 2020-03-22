import random
from Idividual import Individual
from OrderedCrossover import OrderedCrossover
from Loader import Loader
from Mutation import Mutation
from Population import Population
from TournamentSelection import Selection
import xlsxwriter


class GenericAlgorithm:
    def __init__(self, pop_size, gen, Px, Pm, Tour, loader, fileName):
        self.fileName = fileName
        self.loader = loader
        self.Tour = Tour
        self.Pm = Pm
        self.Px = Px
        self.gen = gen
        self.pop_size = pop_size


    def calculate(self):
        outWorkbook = xlsxwriter.Workbook('D:\Program Files\Sztuczna inteligencja\Lista 1\wyniki\\' + self.fileName)
        outSheet = outWorkbook.add_worksheet()
        outSheet.write("A1", "najlepszy")
        outSheet.write("B1", "średni")
        outSheet.write("C1", "najgorszy")
        population = Population(self.pop_size, self.loader)
        m = Mutation(self.Pm)
        cross = OrderedCrossover(self.Px, self.loader)
        ts = Selection(self.Tour)
        generationNumber = 0
        i = 2
        while(generationNumber < self.gen):
            newPopSize = 0
            newPopulation = Population(0, self.loader)
            while(newPopSize < self.pop_size):
                val1 = ts.selection_result(population)
                val2 = ts.selection_result(population)
                ox = cross.crossover(val1, val2)
                mut = m.mutate(ox)
                newPopulation.population_array.append(mut)
                newPopSize+=1
            population = newPopulation
            outSheet.write("A"+str(i), str(selectBest(population.population_array)))
            outSheet.write("B" + str(i), str(avarage(population.population_array)))
            outSheet.write("C" + str(i), str(selectWorst(population.population_array)))
            generationNumber+=1
            i+=1
        outWorkbook.close()

def selectBest(group):
    bestValue = group[0].calculate_travel_length()
    for i in group:
        if i.calculate_travel_length() < bestValue:
            bestValue = i.calculate_travel_length()
    return  bestValue

def avarage(group):
    sum = 0
    for i in group:
        sum += i.calculate_travel_length()
    return  sum/len(group)

def selectWorst(group):
    worstValue = group[0].calculate_travel_length()
    for i in group:
        if i.calculate_travel_length() > worstValue:
            worstValue = i.calculate_travel_length()
    return  worstValue
