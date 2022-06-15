import random as r
print("\n####CSE-422 LAB02 Tamanna Aftoz @18301153####\n")


def create_population(chrom_len):
    popu_len = 2**chrom_len-1
    population = []
    n = 1
    while n <= popu_len:
        chrom = ""
        for i in range(chrom_len):
            gene = str(r.randrange(0, 2))
            chrom += gene
        if chrom not in population:
            population.append(chrom)
            n += 1
    string = '0'*chrom_len
    if string in population:
        population.remove(string)
    return population


def fitness(population, data):
    weight_sum = []
    for chromosome in population:
        weight = 0
        for i in range(len(chromosome)):
            if chromosome[i] == '1':
                if data[i].split()[0] == 'l':
                    weight -= int(data[i].split()[1])
                else:
                    weight += int(data[i].split()[1])
        weight_sum.append(weight)
    return weight_sum


def selection(population):
    index = r.randrange(0, len(population))
    selected_chromosome = population[index]
    return index, selected_chromosome


def crossover(parent1, parent2):  # one point crossover
    index = r.randrange(0, len(parent1))
    offspring1 = parent1[:index]+parent2[index:]
    offspring2 = parent2[:index]+parent1[index:]
    return (offspring1, offspring2)


def mutation(offsprings, chromosome_length):  # Bit flip mutation
    index = r.randrange(0, chromosome_length)
    ret_str = []
    for off in offsprings:
        str_list = list(off)
        if str_list[index] == '1':
            str_list[index] = '0'
            ret_str.append("".join(str_list))
        else:
            str_list[index] = '1'
            ret_str.append("".join(str_list))
    return ret_str


def gene_algo(file_name):
    # taking input
    file = open(file_name, 'r')
    chromosome_length = int(file.readline())
    data = []
    for i in range(chromosome_length):
        data.append(file.readline().replace('\n', ''))
    population = create_population(chromosome_length)
    # iterating the algo for numerous times, if ans not found then returns -1
    iter = 0
    while iter < 1000:
        fit = fitness(population, data)
        if fit.count(0) != 0:
            return population[fit.index(0)]
        ind1, parent1 = selection(population)
        ind2, parent2 = selection(population)
        offsprings = ()
        offsprings = crossover(parent1, parent2)
        # Checking if crossovered fitness is better than parents fitness. If it is than statment inside if block executing
        if min(fitness(parent1, data), key=lambda x: abs(0)) > min(fitness(offsprings[0], data), key=lambda x: abs(0)) or min(fitness(offsprings[1], data), key=lambda x: abs(0)) < min(fitness(parent2, data), key=lambda x: abs(0)):
            population[ind1] = offsprings[0]
            population[ind2] = offsprings[1]
            mutated = ()
            mutated = mutation(offsprings, chromosome_length)
            # Checking if mutated fitness is better than crossovered fitness. If it is than statment inside if block executing
            if min(fitness(mutated[0], data), key=lambda x: abs(0)) < min(fitness(offsprings[0], data), key=lambda x: abs(0)) or min(fitness(offsprings[1], data), key=lambda x: abs(0)) > min(fitness(mutated[1], data), key=lambda x: abs(0)):
                population[ind1] = mutated[0]
                population[ind2] = mutated[1]
        iter += 1
    return -1


print("Checking output for the first sample input : ", gene_algo("input2.1.txt"))
print("Checking output for the second sample input : ", gene_algo("input2.2.txt"))
