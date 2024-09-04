import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import sys #reads command line arguments

'''

Function that reads the command lines from terminal

python ./graph.py --input graph_file.gml --create_random_graph 
--nodes n --constant c --plot --BFS a --output out_graph_file.gml

--input graph_file.gml      : specifies input file. Describes the graphs structure
--create_random_graph       : indicates that a new random graph should be created.
--nodes n                   : number of nodes
--constant c                : probability 
--BFS a                     : specifies the node (a) to compute all the shortest paths
--plot                      : requests that the graph be plotted
--output out_graph_file.gml : where resulting graph should be saved.
'''

def CommandLineArgs(argv):

    inputFile = ''
    create_random_graph = False
    nodes = 0
    constant = 0.0
    probability = 0.0
    plot = False
    BFS = ''
    outputFile = ''


    i = 1
    while i < len(argv):
        if argv[i] == '--input':
            inputFile = argv[i+1]
            i += 2 #moves to next set of arguments
        elif argv[i] == '--create_random_graph':
            print("OUTPUT")
            create_random_graph = True
            i += 1
        elif argv[i] == '--nodes':
            nodes = int(argv[i+1])
            i += 2 
        elif argv[i] == '--constant':
            constant = float(argv[i+1])
            probability = (constant * math.log(nodes)) / nodes
            i += 2 
        elif argv[i] == '--plot':
            plot = True
            i += 1 
        elif argv[i] == '--BFS':
            BFS = argv[i+1]
            i += 2 
        elif argv[i] == '--output':
            outputFile = argv[i+1]
            i += 2 
        else:
            print("Error. Invalid input")
            sys.exit(1)
    return [inputFile, create_random_graph, nodes, probability, plot, BFS, outputFile]


    

def main():

    '''
    #create a graph with no nodes and no edges
    G = nx.Graph()

    #add one note
    G.add_node(2)

    #adding edges
    G.add_edge(1,2)

    #print graphs info
    nx.draw(G, with_labels=True)
    plt.show()
    '''

    input = CommandLineArgs(sys.argv)
    print("HELLO")
    inputFile = input[0]
    create_random_graph = input[1]
    nodes = input[2]
    probability = input[3]
    plot = input[4]
    BFS = input[5]
    outputFile = input[6]

    if inputFile:
        with open(inputFile, "r") as f:
            for line in f:
                pass
    elif create_random_graph:
        if nodes <= 0:
            print("Error. Nodes must be greater than 0.")
        G = nx.erdos_renyi_graph(nodes, probability)
        if plot:
            nx.draw(G, with_labels=True)
            plt.show()


    print(sys.argv[1:])
   



if __name__ == "__main__":
    main()