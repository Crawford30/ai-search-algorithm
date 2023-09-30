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

def greedy_search(graph, start, heuristic):
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

        # Choose the neighbor with the lowest heuristic value
        best_neighbor = min(unvisited_neighbors, key=lambda neighbor: heuristic[neighbor])

        current_node = best_neighbor

    return path


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

    heuristic_values = {"S": 7, "A": 5, "B": 7, "C": 3, "D": 1, "G": 0}

    greedy_path = greedy_search(g.graph, start_node, heuristic_values)

    print("Greedy Search path starting from", start_node, ":", " -> ".join(greedy_path))
