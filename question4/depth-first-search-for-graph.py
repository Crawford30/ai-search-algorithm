#QUESTION 3. Using python implement the following search strategies using for graph search
#a. Depth first search

#Note:: 1. DFS for Graph can contain cycles
#Note:: 2. A state can be visited more than once


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" -> ")
            visited.add(node)
            stack.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)

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

    print("DFS Graph traversal starting from S:")
    dfs(g.graph, "S")
