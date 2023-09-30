#QUESTION 5. Using python implement the following search strategies using for tree search
#b. DFS

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
    
    # To store the order in which states are expanded
    expanded_order = []  

    while queue:
        node = queue.popleft()
         # Record expanded states
        expanded_order.append(node) 

        if node not in visited:
            visited.add(node)
            path.append(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return path, expanded_order

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

    start_node = "S"

    bfs_path, expanded_states = bfs(g.graph, start_node)

    print("BFS path starting from", start_node, ":", " -> ".join(bfs_path))
    print("Expanded states:", " -> ".join(expanded_states))
    unexpanded_states = set(g.graph.keys()) - set(expanded_states)
    print("Unexpanded states:", " -> ".join(sorted(unexpanded_states)))
