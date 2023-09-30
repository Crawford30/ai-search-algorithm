#QUESTION 2.
# Using sets and dictionary libraries represent the graph in Figure 1 into a python graph structure.



# Empty Dictionary to holds the states
directed_graph_dictionary = {}

# Add vertices (nodes) to the directed graph
directed_graph_dictionary['S'] = set(['A', 'B'])
directed_graph_dictionary['A'] = set(['B', 'C'])
directed_graph_dictionary['B'] = set(['C'])
directed_graph_dictionary['C'] = set(['D', 'G'])
directed_graph_dictionary['D'] = set(['G'])
directed_graph_dictionary['G'] = set()

# Print the Directed Graph
for vertex, neighbors in directed_graph_dictionary.items():
    print(f"{vertex} -> {neighbors}")