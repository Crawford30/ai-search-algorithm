#QUESTION 6. For each of the following graph search strategies, print out the order in which states are expanded, the path returned by graph search, as well as the states that are not expanded. In all search algorithms, assume ties are broken in alphabetical order

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

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]
    
    path = {}
    
    # Keep track of expanded states
    expanded_states = []  

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        expanded_states.append(node)
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
            return final_path, expanded_states

        neighbors = graph.get(node, [])
        
        # Sort neighbors by cost and node name
        neighbors.sort(key=lambda x: (x[1], x[0]))  
        for neighbor, neighbor_cost in neighbors:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor))
                path[neighbor] = node

    return None, expanded_states

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
    
    ucs_path, expanded_states = uniform_cost_search(g.graph, start_node, goal_node)

    if ucs_path:
        print("Expanded states:", " -> ".join(expanded_states))
        print("UCS GRAPH SEARCH path from", start_node, "to", goal_node, ":", " -> ".join(ucs_path))
    else:
        print("No path found from", start_node, "to", goal_node)
