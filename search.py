#Search Algorithms

def bingo(me, population, infected): #Fucntion searches for direct infections.
    inf = False
    if me < len(population): #Checks if query is valid.
        if me in infected:
            inf = True
            print('Beacon is already in infected list.')
            return inf
        for contacts in range(0,len(population[me])):
            if population[me][contacts] in infected:
                print('Beacon has had contact with an infected beacon.')
                inf = True
                return inf
        print('Beacon has not had any contacts with infected beacons.')
        return inf

def is_goal(current, goal):
    if current == goal:
        return True
    else:
        return False

def dfs(population, infection, my_node): #Takes in adjacent matrix, infection vector and node of interest.
    finished = False
    for indiv in range(0, len(infection)):
        if is_goal(my_node,indiv):
            print('You are infected')
        elif infection[indiv]:
            to_check = [my_node]
            print('Found Infection')
            #for connection in range(0, len(population[my_node])):
            #    if population[my_node][connection]:
