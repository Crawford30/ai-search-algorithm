#QUESTION 5. Using python implement the following search strategies using for tree search
#a. Depth first search


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]


def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    
    # Stop the traversal when you reach "G", the goal Node
    if node == "G":  
        return
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

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

    visited_nodes = set()
    path = []
    dfs(g.graph, start_node, visited_nodes, path)

    expanded_states = visited_nodes
    unexpanded_states = set(g.graph.keys()) - expanded_states

    print("DFS path starting from", start_node, ":", " -> ".join(path))
    print("Expanded states:", " -> ".join(expanded_states))
    print("Unexpanded states:", " -> ".join(sorted(unexpanded_states)))



