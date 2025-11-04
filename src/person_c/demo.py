"""
Person C - Demo Runner
Loads a Sudoku text file using input_parser and prints stats.
"""

import argparse
from .input_parser import (
    parse_sudoku_file,
    print_grid,
    is_grid_complete,
)


def count_filled_and_empty(grid):
    """Return the number of filled and empty cells."""
    filled = sum(1 for row in grid for cell in row if cell != 0)
    empty = 81 - filled
    return filled, empty


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and display a Sudoku puzzle.")
    parser.add_argument(
        "file",
        nargs="?",
        default="sudoku_easy.txt",
        help="Path to the Sudoku .txt file (default: sudoku_easy.txt)",
    )

    args = parser.parse_args()
    grid = parse_sudoku_file(args.file)

    print("Sudoku Grid:")
    print_grid(grid)

    filled, empty = count_filled_and_empty(grid)

    print("\nStats:")
    print(f"Filled cells: {filled}")
    print(f"Empty cells : {empty}")
    print(f"Solved      : {is_grid_complete(grid)}")