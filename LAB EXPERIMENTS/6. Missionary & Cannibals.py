
from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# Boat position: 0 = Left, 1 = Right

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries must not be outnumbered
    # on either bank when they are present
    if m > 0 and c > m:
        return False

    mr = 3 - m
    cr = 3 - c

    if mr > 0 and cr > mr:
        return False

    return True

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            return path + [state]

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))

    return None

solution = solve()

if solution:
    print("Missionaries and Cannibals Solution")
    for state in solution:
        m, c, boat = state
        print("Left Bank: M =", m, "C =", c,
              "| Right Bank: M =", 3-m, "C =", 3-c,
              "| Boat:", "Left" if boat == 0 else "Right")
else:
    print("No solution found")
