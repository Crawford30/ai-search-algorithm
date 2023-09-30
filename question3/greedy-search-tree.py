#QUESTION 3. Using python implement the following search strategies using for tree search
#d. Greedy Search

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]

def greedy_search(graph, start):
    visited = set()
    path = []

    current_node = start

    while current_node:
        path.append(current_node)
        visited.add(current_node)

        neighbors = graph.get(current_node, [])
        unvisited_neighbors = [n for n in neighbors if n not in visited]

        if not unvisited_neighbors:
            break

        # In a Greedy Search, 
        # choose the neighbor that appears first in the list
        current_node = unvisited_neighbors[0]

    return path

# Usage
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

    greedy_path = greedy_search(g.graph, start_node)

    print("Greedy Search path starting from", start_node, ":", " -> ".join(greedy_path))
