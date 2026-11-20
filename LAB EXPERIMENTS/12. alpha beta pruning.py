
def alphabeta(depth, node, alpha, beta, is_max, values):

    if depth == 2:
        return values[node]

    if is_max:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, node * 2 + i,
                alpha, beta, False, values
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(
                depth + 1, node * 2 + i,
                alpha, beta, True, values
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 2, 9]

result = alphabeta(
    0, 0, float('-inf'), float('inf'), True, values
)

print("Best Value:", result)
