import networkx as nx
import matplotlib.pyplot as plt
import sys

'''
python ./graph.py --input graph_file.gml --create_random_graph 
--nodes n --constant c --plot --BFS a --output out_graph_file.gml


'''

create_random_graph = False
plot = False

def CommandLineArgs(argv):
    i = 0
    while i < len(argv):
        if argv[i] == '--input':
            inputFile = argv[i+1]
            i += 2 #next to next set of arguments
        elif argv[i] == '--create_random_graph':
            create_random_graph = True
            i += 1
        elif argv[i] == '--nodes':
            nodes = argv[i+1]
            i += 2 
        elif argv[i] == '--constant':
            constant = argv[i+1]
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
            print("error")
            sys.exit(1)
        
        return inputFile, create_random_graph, nodes, constant, plot, BFS, outputFile

def main():
    #create a graph with no nodes and no edges
    G = nx.Graph()

    #add one note
    G.add_node(2)

    #adding edges
    G.add_edge(1,2)

    #print graphs info
    nx.draw(G, with_labels=True)
    plt.show()

    print(sys.argv[1:])
   



if __name__ == "__main__":
    main()