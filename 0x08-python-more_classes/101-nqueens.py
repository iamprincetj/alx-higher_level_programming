#!/usr/bin/python3
'''solves the n queen puzzle'''
import sys


def nqueens(n):
    if isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, ro, col):
        for r, c in board:
            if r == ro or c == col or r - c == ro - col or r + c == ro + col:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append([row, col])
                backtrack(board, row + 1)
                board.pop()

    backtrack([], 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
