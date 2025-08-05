from collections import deque

def bfs(graph, start):
    visited = set()        
    queue = deque([start])
    order = []             

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
bfs_order = bfs(graph, start_node)
print("BFS traversal order:", bfs_order)
