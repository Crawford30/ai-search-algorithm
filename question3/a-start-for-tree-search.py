#QUESTION 3. Using python implement the following search strategies using for tree search
#e. A*

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node in self.graph:
            self.graph[node].append((neighbor, cost))
        else:
            self.graph[node] = [(neighbor, cost)]

def astar_search(graph, start, goal, node_heuristics):
    visited = set()
    priority_queue = [(0, start)]
    path = {}
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue

        if current_node == goal:
            final_path = []
            while current_node:
                final_path.append(current_node)
                current_node = path.get(current_node)
            final_path.reverse()
            return final_path

        visited.add(current_node)

        for neighbor, neighbor_cost in graph.get(current_node, []):
            if neighbor in visited:
                continue

            tentative_g_score = g_scores[current_node] + neighbor_cost

            if tentative_g_score < g_scores[neighbor]:
                path[neighbor] = current_node
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + node_heuristics.get(neighbor, 0)  # Use node-specific heuristic
                heapq.heappush(priority_queue, (f_score, neighbor))

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
    
    #Node Heuristic 
    node_heuristics = {"S": 7, "A": 5, "B": 7, "C": 3, "D": 1, "G": 0}
     
    ##A Star Path
    astar_path = astar_search(g.graph, start_node, goal_node, node_heuristics)

    if astar_path:
        print("A* path from", start_node, "to", goal_node, ":", " -> ".join(astar_path))
    else:
        print("No path found from", start_node, "to", goal_node)
