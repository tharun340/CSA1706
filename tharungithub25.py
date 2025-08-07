from collections import deque

class MonkeyBananaProblem:
    def __init__(self):
        self.rooms = ['room1', 'room2', 'room3']
        self.connected = {
            'room1': ['room2'],
            'room2': ['room1', 'room3'],
            'room3': ['room2']
        }
        self.initial_state = ('room1', 'room1', 'room3', False)

    def is_goal(self, state):
        return state[3] == True  

    def get_neighbors(self, state):
        neighbors = []
        monkey, box, banana, has_banana = state
        for new_pos in self.connected[monkey]:
            if new_pos != monkey:
                neighbors.append((
                    (new_pos, box, banana, has_banana),
                    f'move to {new_pos}'
                ))

        if monkey == box:
            for new_pos in self.connected[box]:
                if new_pos != box:
                    neighbors.append((
                        (new_pos, new_pos, banana, has_banana),
                        f'push box to {new_pos}'
                    ))

        if monkey == box == banana and not has_banana:
            neighbors.append((
                (monkey, box, banana, True),
                'climb box and get banana'
            ))

        return neighbors

    def solve(self):
        queue = deque()
        queue.append((self.initial_state, []))
        visited = set()
        visited.add(self.initial_state)

        while queue:
            current_state, path = queue.popleft()

            if self.is_goal(current_state):
                return path

            for neighbor_state, action in self.get_neighbors(current_state):
                if neighbor_state not in visited:
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, path + [action]))

        return None  

if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    solution = problem.solve()
    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
