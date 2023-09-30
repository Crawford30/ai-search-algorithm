import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor, cost):
        if node in self.graph:
            self.graph[node].append((neighbor, cost))
        else:
            self.graph[node] = [(neighbor, cost)]

def astar_search(graph, start, goal, heuristic):
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
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f_score, neighbor))

    return None

# Define a heuristic function (you need to customize this based on your problem)
def heuristic(node, goal):
    # Return an estimate of the cost from node to goal
    # This can be based on distance, straight-line distance, etc.
    # For demonstration purposes, we'll use a simple heuristic (return 0)
    return 0
#("S", "A"), ("S", "B"), ("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("C", "G"), ("D", "G")
# Usage
if __name__ == "__main__":
    g = Graph()

    g.add_edge("S", "A", 1)
    g.add_edge("S", "B", 2)
    g.add_edge("A", "B", 1)
    g.add_edge("A", "G", 5)
    g.add_edge("B", "A", 3)
    g.add_edge("B", "G", 2)

    start_node = "S"
    goal_node = "G"

    astar_path = astar_search(g.graph, start_node, goal_node, heuristic)

    if astar_path:
        print("A* path from", start_node, "to", goal_node, ":", " -> ".join(astar_path))
    else:
        print("No path found from", start_node, "to", goal_node)
