#QUESTION 4. Using python implement the following search strategies using for graph search
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

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

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
    
    # g.add_edge("S", "A")
    # g.add_edge("S", "B")
    # g.add_edge("A", "B")
    # g.add_edge("A", "C")
    # g.add_edge("B", "C")
    # g.add_edge("C", "D")
    # g.add_edge("C", "G")
    # g.add_edge("D", "G")
    # g.add_edge("B", "C")
    # g.add_edge("C", "D")
    # g.add_edge("C", "G")
    # g.add_edge("D", "G")

    print("BFS traversal starting from S:")
    bfs_path = bfs(g.graph, "S")
    print(" -> ".join(bfs_path))
