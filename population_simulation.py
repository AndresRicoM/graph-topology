#Functions for population simulation.
import numpy as np
import math
import random

def get_poplist(url):
    poplist = []
    # open file and read the content in a list
    with open(url, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            poplist.append(currentPlace)
    return poplist


def get_popmat(url):
    popmat = np.genfromtxt(url, delimiter = ',')
    return popmat

def get_infectvect(url):
    infectedvect = np.genfromtxt(url, delimiter = ',')
    return infectedvect

def adjacent_list(list_size, max_encounters):
    complete = []
    for pop in range(0,list_size):
        encounters = random.randint(0,max_encounters)
        indiv_list = []
        for enc in range(0, encounters):
            prox = random.randint(0, list_size-1)
            if prox != pop:
                indiv_list.append(prox)
        complete.append(indiv_list)
    return complete

def adjacent_mat(population): #Creates Adjacent Matrix Structure From Adjacent lists
    matrix = np.zeros((len(population), len(population)))
    for list in range(0,len(population)):
        for element in range(0,len(population[list])):
            matrix[list,(population[list][element])] = True
            matrix[(population[list][element]),list] = True
    return matrix

def infect_2d(population, probability):
    inf = []
    non_inf = []
    for element in range(0,len(population)):
        if random.random() > probability:
            inf.append(element)
        else:
            non_inf.append(element)
    complete_inf = []
    complete_inf.append(inf)
    complete_inf.append(non_inf)
    return complete_inf

def binary_vect(population, probability):
    complete_inf = []
    for nodes in range(0, len(population)):
        if random.random() > probability:
	        complete_inf.append(1)
        else:
            complete_inf.append(0)
    return complete_inf

def simple_pop(pop_size, encounters):
    complete_pop = np.zeros((encounters + 1, pop_size))
    complete_pop = np.arange(1, pop_size + 1,1)

def sim_population(pop_size, encounters): #Takes as argument population size and encounters.
    full_history = np.zeros((encounters, pop_size * 2))
    population = np.arange(1,pop_size + 1, .5)
    for cols in range(0, population.shape[0]-1):
        if not cols % 2:
            full_history[0:,cols:cols+2] = sim_history(encounters, pop_size)
    final = np.vstack((population, full_history))
    return final

def sim_history(encounters, max_id): #Takes as argument encounters.
    history = np.zeros((encounters, 2))
    history[:,0] = np.arange(1,encounters + 1,1)
    for rows in range(0, history.shape[0]):
        history[rows, 1] = round(random.randint(1,max_id))#Sequential Time Stamp
    return history
