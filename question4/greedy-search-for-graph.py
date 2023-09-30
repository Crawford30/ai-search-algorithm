#QUESTION 3. Using python implement the following search strategies using for graph search
#d. Greedy Search
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node in self.graph:
            self.graph[node].append((neighbor, cost))
        else:
            self.graph[node] = [(neighbor, cost)]

def greedy_search(graph, start, goal, node_heuristics):
    visited = set()
    path = []

    current_node = start

    while current_node:
        path.append(current_node)
        visited.add(current_node)

        if current_node == goal:
            break

        neighbors = graph.get(current_node, [])
        unvisited_neighbors = [(n, cost) for n, cost in neighbors if n not in visited]

        if not unvisited_neighbors:
            break

        # Choose the neighbor with the lowest heuristic value
        current_node = min(unvisited_neighbors, key=lambda x: node_heuristics[x[0]])

    return path

if __name__ == "__main__":
    g = Graph()

    g.add_edge("S", "A", 3)
    g.add_edge("S", "B", 1)
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 3)
    g.add_edge("C", "D", 4)
    g.add_edge("C", "G", 4)
    g.add_edge("D", "G", 1)
    g.add_edge("G", "G", 0)

    start_node = "S"
    goal_node = "G"

    node_heuristics = {"S": 7, "A": 5, "B": 7, "C": 3, "D": 1, "G": 0}

    greedy_path = greedy_search(g.graph, start_node, goal_node, node_heuristics)

    # Convert the tuples to strings for printing
    path_str = " -> ".join([node[0] for node in greedy_path])

    print("Greedy Search GRAPH path from", start_node, "to", goal_node, ":", path_str)
