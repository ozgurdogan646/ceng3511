import random as rd
import numpy as np

#%% initilazing population(binary representation)

def initilazepopulation(popSize,number_of_genes):
    population = []
    for i in range(popSize):
        temp = []
        for j in range(len(w)):
            temp.append(rd.randint(0,1))
        population.append(temp)
    return population
#%% determine fitness functions
def fitness_functions(population_arr,capacity,weights,values):
    fitness_values = {}
    for i,chromosome in enumerate(population_arr):
        total_weight = 0 
        total_value = 0
        for j in chromosome :
            if(j == 1):
                total_weight += weights[chromosome.index(j)]
                total_value += values[chromosome.index(j)]
        if(total_weight > capacity):
            fitness_values[i] = 0
        else : 
            fitness_values[i] = total_value
    return fitness_values
#%% parent selection            
def get_probability_list(fitness_functions):
    fitness = fitness_functions.values()
    total_fit = float(sum(fitness))
    relative_fitness = [f/total_fit for f in fitness]
    probabilities = [sum(relative_fitness[:i+1]) 
                     for i in range(len(relative_fitness))]
    return probabilities

def roulette_wheel_pop(population, probabilities):
    chosen = []
    for n in range(2):
        r = rd.random()
        for (i, individual) in enumerate(population):
            if r <= probabilities[i]:
                chosen.append(list(individual))
                break
    return chosen


def k_tournament_selection(population,k_value,fitness_functions):
    chosen = []
    for i in range(3):
        ind = population[rd.randrange(0,len(population)-1)]
        if chosen == [] or fitness_functions[population.index(ind)] > fitness_functions[chosen[0]]:
            chosen = ind
    return chosen
#%% crossover
def crossover(p1, p2 , n):
    child = []
    p1 = list(p1)
    p2 = list(p2)
    rand_number = [0]
    for i in range(n):
        random_number = rd.randrange(1,len(p1)-1)
        rand_number.append(random_number)
    for j in range(1,len(rand_number)):
        p1[rand_number[j-1]:rand_number[j]] , p2[rand_number[j-1]:rand_number[j]] = p2[rand_number[j-1]:rand_number[j]] , p1[rand_number[j-1]:rand_number[j]]
    p1 = ''.join(str(p1))
    p2 = ''.join(str(p2))
    child.append(p1)
    child.append(p2)
    return child
#%% survival selection
def fitness_based_selection(population,current_fitness_functions,new_generation):
    current_fitness_functions_values = list(current_fitness_functions.values())
    current_fitness_functions_keys = list(current_fitness_functions.keys())
    population[current_fitness_functions_keys[current_fitness_functions_values.index(min(current_fitness_functions_values))]] = new_generation[0]
    population[current_fitness_functions_keys[current_fitness_functions_values.index(min(current_fitness_functions_values))]] = new_generation[1]
    return population

#%% mutation
def mutation(new_generation):
    for i in new_generation :
        bit = rd.randrange(0,len(new_generation[0]))
        if(i[bit] == 0):
            i[bit] = 1
        else :
            i[bit] = 0
    return new_generation
#%%

fc = open('./c.txt', 'r')
fw = open('./w.txt', 'r')
fv = open('./v.txt', 'r')
fout = open('./out.txt', 'w')


c = int(fc.readline())
w = []
v = []
for line in fw:
    w.append(int(line))
for line in fv:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

popSize = int(input('Size of population : ')) #popülasyondaki parent sayısı
genNumber = int(input('Max number of generation : '))
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')
parentSelection = int(input('Which one? '))
if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))

print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))

print('\nMutation Probability\n---------------------------')
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
#elitism = bool(input('Elitism? (Y or N) ' ))


print('\n----------------------------------------------------------')
print('initalizing population')
population = initilazepopulation(popSize,len(w))
for i in range(genNumber):
    fitness_functions1 = fitness_functions(population,c,w,v)
    if parentSelection == 1 :
        probabilities = get_probability_list(fitness_functions1)
        selected_parents = roulette_wheel_pop(population,probabilities)
    else :
        selected_parents = []
        for i in range(2):
            selected_parents.append(k_tournament_selection(population,3,fitness_functions1))
    new_generation = []
    for i in range(2):
        child = crossover(selected_parents[i-1],selected_parents[i-1],n)
    new_generation.append(eval(child[0]))
    new_generation.append(eval(child[1]))
    mutation_rate = rd.random()
    if(mutation_rate<mutProb):
        new_generation = mutation(new_generation)
    new_generation_fitness_values = fitness_functions(new_generation,c,w,v)

    population = fitness_based_selection(population,fitness_functions1,new_generation)
    fitness_functions1 = fitness_functions(population,c,w,v)
    
output_values = list(fitness_functions1.values())
output_keys = list(fitness_functions1.keys())

selected_chromosome = population[output_keys[output_values.index(max(output_values))]]
selected_weight = 0
for i,gen in enumerate(selected_chromosome):
    if  gen == 1:
        selected_weight += w[i]
selected_value = max(output_values)


#%%  

fout.write("chromosome: {} ".format(selected_chromosome)+"\n")
fout.write("weight: {} ".format(selected_weight)+"\n")
fout.write("value: {} ".format(selected_value)+"\n")
fout.close() 







