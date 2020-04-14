#Search Algorithms

def bingo(me, list, infected): #Fucntion searches for direct infections.
    inf = False
    if me in infected:
        inf = True
        print('Beacon is already in infected list.')
        return inf
    for contacts in range(0,len(list)):
        if list[contacts] in infected:
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

def explore_node(node, node_list): #Expands Nodes and Adds to List
    to_explore = []
    for nodes in range(0,len(node_list)):
        to_explore.append(node_list[nodes])
    return to_explore

def dfs(population, infection, my_node): #Takes in adjacent matrix, infection vector and node of interest.
    solution_list = []
    checked = []
    exploring = [my_node]
    contact = False
    for items in range(0, len(infection)):
        while exploring:
            #print('Current list: ', exploring)
            current_node = exploring[0]
            checked.append(current_node)
            if is_goal(current_node, infection[items]):
                #Add to Solution Space
                solution_list.append(current_node)
                contect = True
                print('Indirect connection has been found.')
                return True
            else:
                to_add = explore_node(current_node,population[current_node])
                exploring.pop(0)
                for items in range(0,len(to_add)):
                    if not to_add[items] in checked:
                        exploring.append(to_add[items])
    print('No indirect connections found.')
    return False
