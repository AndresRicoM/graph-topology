import numpy as np
import math
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from population_simulation import *
from mayavi import mlab
from search import *
import os

if __name__ == '__main__':

    print('Enter Population')
    pop_name = input()
    print('Beacon to Check')
    beacon = int(input())

    main_path = os.getcwd()
    list_path = main_path + '/populations/lists/' + '/' + pop_name + '.txt'
    #mat_path = main_path + '/populations/matrices/' + '/' + pop_name + '.txt'
    inf_path = main_path + '/populations/infected/' + '/' + pop_name + '.txt'

    list = get_poplist(list_path)
    #mat = get_popmat(mat_path)
    infect = get_infectvect(inf_path)

    print('Beacon: ', beacon, 'Quarentine: ' , bingo(beacon,list,infect))

    """
    for i in range (0, len(list)):
        print('Beacon: ', i, 'Quarentine: ' , bingo(i,list,infect))
    """
