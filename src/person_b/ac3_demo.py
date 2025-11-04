"""
Person B - AC-3 Algorithm Demo
"""

import sys
import os
from collections import deque

# Join path folders to person a
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.person_a.csp_model import SudokuCSP
from src.person_b.ac3 import ac3, print_queue_log


# Helper: print Sudoku grid
def print_puzzle(puzzle):
    for i, row in enumerate(puzzle):
        if i % 3 == 0 and i != 0:
            print("  " + "-" * 21)
        row_str = "  "
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(val) if val != 0 else ".") + " "
        print(row_str)

# Demo Runner
def run_demo(puzzles):
    for n, puzzle in enumerate(puzzles, start=1):
        print("\n========================")
        print(f"Sudoku Puzzle {n} - Before AC-3")
        print("========================")
        print_puzzle(puzzle)

        csp = SudokuCSP(puzzle)
        print("\nRunning AC-3 ...")
        is_consistent, is_solved, queue_log = ac3(csp)

        print("\nSudoku Puzzle", n, "- After AC-3")
        print_puzzle(csp.get_puzzle())

        print(f"\nResult: {'Arc Consistent' if is_consistent else 'Inconsistent'}")
        print(f"Solved: {is_solved}")
        print_queue_log(queue_log, limit=5)

# Example puzzles (replace during live meeting)
puzzle1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

puzzle2 = [
    [0, 0, 0, 0, 7, 0, 0, 0, 9],
    [0, 3, 0, 0, 0, 8, 1, 0, 0],
    [0, 0, 1, 0, 0, 9, 0, 0, 4],
    [0, 0, 0, 7, 0, 0, 9, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 3, 0, 0, 2, 0, 0, 0],
    [7, 0, 0, 5, 0, 0, 2, 0, 0],
    [0, 0, 4, 8, 0, 0, 0, 3, 0],
    [3, 0, 0, 0, 9, 0, 0, 0, 0]
]

if __name__ == "__main__":
    print("\n--------------------------------")
    print("Person B - AC-3 Algorithm Demo")
    print("--------------------------------")
    run_demo([puzzle1, puzzle2])
