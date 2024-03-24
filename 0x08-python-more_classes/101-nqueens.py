#!/usr/bin/python3
import sys


def print_solution(board):
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row):
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = None


def nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [None] * n
    solve_nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
