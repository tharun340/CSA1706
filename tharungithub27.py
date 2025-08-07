import heapq

def best_first_search(start, goal, graph, heuristic):
    """
    graph: dict of {node: [(neighbor, cost), ...]}
    heuristic: dict of {node: heuristic_cost}
    Returns: path, total cost
    """
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        h_cost, cost_so_far, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, cost_so_far

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, step_cost in graph.get(current, []):
            if neighbor not in closed_set:
                new_cost = cost_so_far + step_cost
                heapq.heappush(open_list, (heuristic.get(neighbor, float('inf')), new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'a': [('b', 1), ('c', 4)],
        'b': [('d', 2)],
        'c': [('d', 1)],
        'd': [('e', 5)],
        'e': []
    }

    heuristic = {
        'a': 7,
        'b': 6,
        'c': 2,
        'd': 1,
        'e': 0
    }

    path, cost = best_first_search('a', 'e', graph, heuristic)
    if path:
        print(f"Path found: {' -> '.join(path)} with total cost {cost}")
    else:
        print("No path found.")
