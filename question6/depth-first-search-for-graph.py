#QUESTION 6. For each of the following graph search strategies, print out the order in which states are expanded, the path returned by graph search, as well as the states that are not expanded. In all search algorithms, assume ties are broken in alphabetical order
#a. Depth first search

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
