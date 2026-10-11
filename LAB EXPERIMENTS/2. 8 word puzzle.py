from heapq import heappush, heappop

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)
    return distance

def solve(start):
    queue = []
    heappush(queue, (heuristic(start), start))
    parent = {start: None}
    visited = set()

    while queue:
        _, state = heappop(queue)

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                pos = nr * 3 + nc
                new_state = list(state)
                new_state[zero], new_state[pos] = (
                    new_state[pos], new_state[zero]
                )
                new_state = tuple(new_state)

                if new_state not in visited and new_state not in parent:
                    parent[new_state] = state
                    heappush(queue, (
                        heuristic(new_state), new_state
                    ))

    return None

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

print("Initial Puzzle:")
display(start)

print("Goal State:")
display(goal)

print("Steps to Reach Goal:")

path = solve(start)

if path:
    for step in path[1:]:
        display(step)
    print("Goal State Reached!")
else:
    print("No solution found.")
