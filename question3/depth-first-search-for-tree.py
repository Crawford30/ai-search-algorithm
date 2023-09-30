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
    if node == "G":  # Stop the traversal when you reach  "G", goal Node
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
   
    # g.add_edge("S", "A")
    # g.add_edge("S", "B")
    # g.add_edge("A", "B")
    # g.add_edge("A", "G")
    # g.add_edge("B", "A")
    # g.add_edge("B", "G")
    # g.add_edge("B", "A")
    # g.add_edge("B", "G")
    # g.add_edge("A", "B")
    # g.add_edge("A", "G")
    
    
    # g.add_edge("S", "A")
    # g.add_edge("S", "B")
    # g.add_edge("A", "B")
    # g.add_edge("A", "C")
    # g.add_edge("B", "C")
    # g.add_edge("C", "D")
    # g.add_edge("C", "G")
    # g.add_edge("D", "G")

    print("DFS traversal starting from S:")
    visited_nodes = set()
    path = []
    dfs(g.graph, "S", visited_nodes, path)
    print(" -> ".join(path))



