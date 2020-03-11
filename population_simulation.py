#Functions for population simulation.
import numpy as np
import math
import random

def adjacent_pop(pop_size, max_encounters):
    complete = []
    for pop in range(0,pop_size):
        encounters = random.randint(1,max_encounters)
        indiv_list = []
        for enc in range(0, encounters):
            prox = random.randint(0, pop_size-1)
            if prox != pop:
                indiv_list.append(prox)
        complete.append(indiv_list)
    print(complete)
    return complete

def adjacent_mat(population): #Creates Adjacent Matric Structure From Adjacent lists
    matrix = np.zeros((len(population), len(population)))
    for list in range(0,len(population)):
        for element in range(0,len(population[list])):
            matrix[list,(population[list][element])] = True
            matrix[(population[list][element]),list] = True
    return matrix

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

def rand_infect(id, prob): #Randomly infects population individuals.
    infection_vect = np.zeros((1, ))

print(adjacent_mat(adjacent_pop(60000,23)))
