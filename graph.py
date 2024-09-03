import networkx as nx
import matplotlib.pyplot as plt

#create a graph with no nodes and no edges
G = nx.Graph()

#add one note
G.add_node(2)

#adding edges
G.add_edge(1,2)

#print graphs info
nx.draw(G, with_labels=True)
plt.show()