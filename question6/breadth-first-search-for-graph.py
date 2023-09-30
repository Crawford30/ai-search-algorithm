#QUESTION 6. For each of the following graph search strategies, print out the order in which states are expanded, the path returned by graph search, as well as the states that are not expanded. In all search algorithms, assume ties are broken in alphabetical order
#b. BFS

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []
    expanded_states = []

    while queue:
        node = queue.popleft()
        expanded_states.append(node)
        if node not in visited:
            visited.add(node)
            path.append(node)
            neighbors = graph.get(node, [])
            neighbors.sort()  # Sort the neighbors alphabetically
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return path, expanded_states

if __name__ == "__main__":
    g = Graph()
   
    g.add_edge("S", "A")
    g.add_edge("S", "B")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("C", "G")
    g.add_edge("D", "G")
    
   
    print("BFS traversal starting from S:")
    bfs_path, expanded_states = bfs(g.graph, "S")
    print("Expanded states:", " -> ".join(expanded_states))
    print("Path Returned:", " -> ".join(bfs_path))
    unexpanded_states = set(g.graph.keys()) - set(expanded_states)
    unexpanded_states = sorted(unexpanded_states) #Sort the unexpanded states alphabetically
    print("Unexpanded states:", " -> ".join(unexpanded_states))
