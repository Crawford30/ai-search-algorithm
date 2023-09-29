# Create an empty directed graph
directed_graph = {}

# Add vertices (nodes) to the directed graph
directed_graph['A'] = set(['B', 'C'])
directed_graph['B'] = set(['D', 'E'])
directed_graph['C'] = set(['F'])
directed_graph['D'] = set()
directed_graph['E'] = set(['F'])
directed_graph['F'] = set()

# Printing the directed graph
for vertex, neighbors in directed_graph.items():
    print(f"{vertex} -> {neighbors}")