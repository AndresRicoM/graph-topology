#Functions for population simulation.
import numpy as np
import math
import random

#Simulate Data
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

print(sim_population(685094, 23))
