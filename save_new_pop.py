import sys
import os
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from population_simulation import *
from mayavi import mlab

if __name__ == '__main__':

    main_path = os.getcwd()
    print(main_path)

    print('Input desired name for file...')
    filename = input()
    filename = filename + '.txt'

    file = open(main_path + '/populations/' + filename, 'w+')

    print('What population size do you want?')
    population_size = int(input())

    print('What number of encounters do you want?')
    possible_ecnounters = int(input())

    print('Simulating Population')
    population = adjacent_list(population_size, possible_ecnounters)
    print(population)
    population_mat = adjacent_mat(population)

    for item in population:
        file.write("%s\n" % item)
