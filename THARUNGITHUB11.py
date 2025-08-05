def is_consistent(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_consistent(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtracking(assignment, regions, colors, neighbors)
            if result:
                return result
            # Backtrack
            del assignment[region]

    return None
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

assignment = {}

solution = backtracking(assignment, regions, colors, neighbors)

if solution:
    print("Map Coloring Solution:")
    for region in regions:
        print(f"{region}: {solution[region]}")
else:
    print("No solution found.")
