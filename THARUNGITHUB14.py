import math

# Alpha-Beta pruning function
def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta):
    # Base case: leaf node
    if depth == 3:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf
        # Recur for left and right children
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Prune the remaining branches
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        # Recur for left and right children
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Prune the remaining branches
            if beta <= alpha:
                break
        return best

# Example usage
if __name__ == "__main__":
    # Example tree values at depth 3 (leaf nodes)
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    print("Optimal value:", alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf))
