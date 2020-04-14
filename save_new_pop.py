import sys
import os
import numpy as np
import math
import random
import numpy as np
import random
from population_simulation import *
import pickle


if __name__ == '__main__':

    main_path = os.getcwd()
    print(main_path)

    print('Input desired name for file...')
    filename = input()
    filename = filename + '.txt'

    #list_file = open(main_path + '/populations/lists/' + filename, 'w+')
    #mat_file = open(main_path + '/populations/matrices/' + filename, 'w+')
    #infect_file = open(main_path + '/populations/infected/' + filename, 'w+')

    print('What population size do you want?')
    population_size = int(input())

    print('What number of encounters do you want?')
    possible_ecnounters = int(input())

    print('Probability of Infection?')
    infect_prob = float(input())

    print('Simulating Population')
    population = adjacent_list(population_size, possible_ecnounters)
    population_mat = adjacent_mat(population)
    infect_list = infected_list(population, infect_prob)

    with open(main_path + '/populations/lists/' + filename, "wb") as fp:   #Pickling
        pickle.dump(population, fp)

    with open(main_path + '/populations/matrices/' + filename, "wb") as fp:   #Pickling
        pickle.dump(population_mat, fp)

    with open(main_path + '/populations/infected/' + filename, "wb") as fp:   #Pickling
        pickle.dump(infect_list, fp)

    """
    for item in population:
        list_file.write("%s\n" % item)

    for item in infect_list:
        infect_file.write("%s\n" % item)

    np.savetxt(mat_file, population_mat, delimiter=',')
    """
