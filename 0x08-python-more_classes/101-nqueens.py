#!/usr/bin/python3

def is_valid(board, row, col):
    """check if it's safe to place the queen at (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_sol(board):
    """print N-Queens board"""
    n = len(board)
    for row in range(n):
        line = ["Q" if col == board[row] else "." for col in range(n)]
        print(" ".join(line))
    print()


def solve_nqueens(n):
    """solve N-Queens using backtracking"""
    def backtrack(board, row):
        if row == n:
            print_sol(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    if n < 4:
        print("N must be at least 4")
        return
    board = [-1] * n
    backtrack(board, 0)


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        exit(1)
