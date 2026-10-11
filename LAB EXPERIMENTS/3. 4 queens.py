N = 4

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0:
            if board[i][col - (row - i)] == 1:
                return False

        if col + (row - i) < N:
            if board[i][col + (row - i)] == 1:
                return False

    return True

def solve(board, row):
    if row == N:
        print_solution(board)
        return True

    found = False

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, row + 1):
                found = True

            board[row][col] = 0

    return found

board = [[0 for _ in range(N)] for _ in range(N)]

print("Solutions for 4 Queens Problem:")
if not solve(board, 0):
    print("No solution found")
