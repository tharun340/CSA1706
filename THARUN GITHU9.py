import sys

def tsp(graph):
    """
    Solve the Traveling Salesman Problem using Held-Karp DP approach.
    
    graph: 2D list or matrix with distances between cities.
           graph[i][j] = distance from city i to city j.
           
    Returns: (min_cost, path) tuple.
    """
    n = len(graph)
    all_visited = (1 << n) - 1  # bitmask with all cities visited

    # dp[mask][i] = minimum cost to visit subset mask ending at city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    # Starting at city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                new_cost = dp[mask][last] + graph[last][nxt]
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost
                    parent[new_mask][nxt] = last
    min_cost = float('inf')
    last_city = -1
    for i in range(1, n):
        cost = dp[all_visited][i] + graph[i][0]
        if cost < min_cost:
            min_cost = cost
            last_city = i
    path = []
    mask = all_visited
    curr = last_city
    while curr != -1:
        path.append(curr)
        temp = parent[mask][curr]
        mask = mask & ~(1 << curr)
        curr = temp
    path.append(0)
    path.reverse()

    return min_cost, path
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, best_path = tsp(graph)
print("Minimum cost:", min_cost)
print("Best path:", best_path)
