#Search Algorithms

def bingo(me, population, infected):
    if me < len(population):
        for elems in range(0, len(population[me])):
            if population[me][elems] in infected:
                print('Direct Conatct!')
    else:
        print("Invalid Input")

def is_goal(current, goal):
    if current == goal:
        return True
    else:
        return False

def bingo(comparable_mat, self):
    for indiv in range(0, len(comparable_mat)):
        if self == comparable_mat[]

def dfs(population, infection, my_node): #Takes in adjacent matrix, infection vector and node of interest.
    finished = False
    for indiv in range(0, len(infection)):
        if is_goal(my_node,indiv):
            print('You are infected')
        elif infection[indiv]:
            to_check = [my_node]
            print('Found Infection')
            for connection in range(0, len(population[my_node])):
                if population[my_node][connection]:
