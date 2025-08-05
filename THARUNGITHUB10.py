import heapq

def a_star(graph, start, goal, heuristic):
    """
    graph: dict of nodes with neighbors and edge costs
           e.g. {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, ...}
    start: start node
    goal: goal node
    heuristic: function(node) -> estimated cost from node to goal

    Returns:
        path (list): shortest path from start to goal
        cost (float): total cost of the path
    """
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start), 0, start, [start]))

    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic(neighbor)
                heapq.heappush(open_set, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')


def heuristic(node):
    h_values = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 0,  # goal node
    }
    return h_values.get(node, float('inf'))
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'C': 6, 'D': 1},
    'C': {'D': 2, 'E': 5},
    'D': {'E': 1},
    'E': {}
}

start_node = 'A'
goal_node = 'E'

path, cost = a_star(graph, start_node, goal_node, heuristic)
if path:
    print(f"Shortest path: {path} with cost: {cost}")
else:
    print("No path found.")
