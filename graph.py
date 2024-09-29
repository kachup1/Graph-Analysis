import networkx as nx
import matplotlib.pyplot as plt
import math
import sys

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
def CommandLineArgs(argv): #parses through the command line arguments
    inputFile = ''
    create_random_graph = False
    nodes = 0
    constant = 0.0
    probability = 0.0
    plot = False
    BFS = ''
    outputFile = ''

    #loops through command line arguments and handles errors if invalid inputs are provided
    i = 1
    while i < len(argv):
        if argv[i] == '--input':
            inputFile = argv[i+1]
            if not inputFile.endswith('.gml'):
                print("Error: Input file must be of type .gml")
                sys.exit(1)
            i += 2
        elif argv[i] == '--create_random_graph':
            create_random_graph = True
            i += 1
        elif argv[i] == '--nodes':
            try:
                nodes = int(argv[i+1])
                i += 2
            except ValueError:
                print("Error: --nodes must be an integer.")
                sys.exit(1)
        elif argv[i] == '--constant':
            try:
                constant = float(argv[i+1])
                probability = (constant * math.log(nodes)) / nodes
                i += 2
            except ValueError:
                print("Error: --constant must be a float.")
                sys.exit(1)
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
            print(f"Error: Invalid argument {argv[i]}")
            sys.exit(1)
    
    return [inputFile, create_random_graph, nodes, probability, plot, BFS, outputFile]

#main function
def main():
    input = CommandLineArgs(sys.argv) #gets command line arguments
    
    inputFile = input[0]
    create_random_graph = input[1]
    nodes = input[2]
    probability = input[3]
    plot = input[4]
    BFS = input[5]
    outputFile = input[6]

    #loads the graph from a file or it creates a random graph
    if inputFile:
        G = nx.read_gml(inputFile)
    elif create_random_graph:
        if nodes <= 0:
            print("Error. Nodes must be greater than 0.")
            sys.exit(1)
        G = nx.erdos_renyi_graph(nodes, probability)#built in function for erdos random graph
        G = nx.relabel_nodes(G, lambda x: str(x))#converts to strings
        if plot:
            plt.figure() 
            nx.draw( G, with_labels=True, node_size=700, font_size=12, node_color='pink', edge_color='purple', font_weight='bold')
            plt.show()

    #performs bfs 
    if BFS:
        if BFS not in G:
            print(f"Error. Node {BFS} does not exist in the graph.")
            sys.exit(1)
        elif BFS and input:
            bfs_tree = nx.bfs_tree(G, source=BFS) #computes BFS tree
            
            # NetworkX func - gets positions for the BFS tree
            pos = nx.bfs_layout(bfs_tree, BFS)
            
            #draws the BFS tree 
            plt.figure()  
            nx.draw(bfs_tree, pos, with_labels=True, node_size=700, font_size=12, node_color='pink', edge_color='purple', font_weight='bold')
            plt.title(f"BFS Tree from Node {BFS}")
            plt.show()

    #saves graph to file
    if outputFile:
        nx.write_gml(G, outputFile)

if __name__ == "__main__":
    main()
