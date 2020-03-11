import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from population_simulation import *
from mayavi import mlab
import random

def flat_graph_net(population, infection):
	graph = nx.DiGraph(population)
	fig = plt.figure()
	pos = nx.spring_layout(graph)
	nx.draw_networkx_nodes(graph,pos, node_size = 20, nodelist = infection[0], node_color = 'xkcd:red', with_labels = True)
	nx.draw_networkx_nodes(graph,pos, node_size = 10, nodelist = infection[1], node_color = 'xkcd:green', with_labels = True)
	nx.draw_networkx_edges(graph,pos, edge_list = nx.to_edgelist(graph),edge_color = 'w', arrows = False)
	#fig.set_facecolor("#00000F")
	fig.set_facecolor('xkcd:black')
	plt.axis('off')
	plt.show()


def d3_graph_net(population, probability):
	print(population)
	mlab.options.offscreen = False
	graph = nx.DiGraph(population)
	#G = nx.convert_node_labels_to_integers(graph)
	fig = plt.figure()
	#pos = nx.spring_layout(graph, dim=3) #, k = 5)
	pos = nx.random_layout(graph, dim=3)
	xyz = np.array([pos[v] for v in sorted(graph)])
	print(xyz)
	scalars = np.zeros(len(population))
	for nodes in range(0, len(scalars)):
		if random.random() > probability:
			scalars[nodes] = 1
	print(scalars)
	mlab.figure(1, bgcolor=(0, 0, 0))
	mlab.clf()
	pts = mlab.points3d(xyz[:, 0], xyz[:, 1], xyz[:, 2],
	                    scalars,
	                    scale_factor=0.025,
	                    scale_mode='none',
	                    colormap='blue-red',
	                    resolution=50)

	pts.mlab_source.dataset.lines = np.array(list(graph.edges()))
	tube = mlab.pipeline.tube(pts, tube_radius=0.005)
	mlab.pipeline.surface(tube, color=(1, 1, 1), opacity = .05)

	mlab.show()

d3_graph_net(adjacent_mat(adjacent_pop(50,10)), .85)

"""
#nx.draw_networkx_nodes(graph,pos, node_size = 20, nodelist = infection[0], node_color = 'xkcd:red', with_labels = True)
#nx.draw_networkx_nodes(graph,pos, node_size = 10, nodelist = infection[1], node_color = 'xkcd:green', with_labels = True)
#nx.draw_networkx_edges(graph,pos, edge_list = nx.to_edgelist(graph),edge_color = 'w', arrows = False)
#fig.set_facecolor("#00000F")
# some graphs to try
# H=nx.krackhardt_kite_graph()
# H=nx.Graph();H.add_edge('a','b');H.add_edge('a','c');H.add_edge('a','d')
# H=nx.grid_2d_graph(4,5)
H = nx.cycle_graph(20)

# reorder nodes from 0,len(G)-1
G = nx.convert_node_labels_to_integers(H)
# 3d spring layout
pos = nx.spring_layout(G, dim=3)
# numpy array of x,y,z positions in sorted node order
xyz = np.array([pos[v] for v in sorted(graph)])
# scalar colors
scalars = np.array(list(G.nodes())) + 5

mlab.figure(1, bgcolor=(0, 0, 0))
mlab.clf()

pts = mlab.points3d(xyz[:, 0], xyz[:, 1], xyz[:, 2],
                    scalars,
                    scale_factor=0.1,
                    scale_mode='none',
                    colormap='Blues',
                    resolution=20)

pts.mlab_source.dataset.lines = np.array(list(G.edges()))
tube = mlab.pipeline.tube(pts, tube_radius=0.01)
mlab.pipeline.surface(tube, color=(0.8, 0.8, 0.8))

#mlab.savefig('mayavi2_spring.png')
#
mlab.show() # interactive window
"""
