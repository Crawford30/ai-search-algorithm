#QUESTION 5. Using python implement the following search strategies using for tree search
#c. UCS

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node in self.graph:
            self.graph[node].append((neighbor, cost))
        else:
            self.graph[node] = [(neighbor, cost)]

def ucs(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]
    path = {}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            final_path = []
            while node != start:
                final_path.append(node)
                node = path[node]
            final_path.append(start)
            final_path.reverse()
            return final_path

        for neighbor, neighbor_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor))
                path[neighbor] = node

    return None

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
    
    visited_nodes = set()
    ucs_path = ucs(g.graph, start_node, goal_node)
    expanded_states = visited_nodes
    unexpanded_states = set(g.graph.keys()) - expanded_states #Remove expanded states from the graph

    if ucs_path:
        print("UCS path from", start_node, "to", goal_node, ":", " -> ".join(ucs_path))
        print("Expanded states:", " -> ".join(expanded_states))
        print("Unexpanded states:", " -> ".join(sorted(unexpanded_states)))
    else:
        print("No path found from", start_node, "to", goal_node)
