"""
Person C - Input Handler & Visual Logger
Parses Sudoku text files and pretty-prints grids.
"""

from __future__ import annotations
from typing import List

Grid = List[List[int]]
ALLOWED_EMPTY = {'.', '0', '_', '-'}


def parse_sudoku_file(file_path: str) -> Grid:
    """
    Parse a Sudoku .txt file into a 9x9 grid of ints (0 = blank).
    Raises ValueError on malformed input.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        raw_lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(raw_lines) != 9:
        raise ValueError(f"Expected 9 non-empty lines, got {len(raw_lines)} in {file_path}")

    grid: Grid = []
    for i, line in enumerate(raw_lines):
        line = line.replace(" ", "")
        if len(line) != 9:
            raise ValueError(f"Line {i+1} must have 9 characters after removing spaces; got {len(line)}.")

        row: List[int] = []
        for ch in line:
            if ch in ALLOWED_EMPTY:
                row.append(0)
            elif ch.isdigit() and ch != '0':
                val = int(ch)
                if not 1 <= val <= 9:
                    raise ValueError(f"Invalid digit '{ch}' at line {i+1}.")
                row.append(val)
            else:
                raise ValueError(
                    f"Invalid character '{ch}' at line {i+1}. "
                    f"Use digits 1-9 or one of {sorted(ALLOWED_EMPTY)} for blanks."
                )
        grid.append(row)

    return grid


def format_grid(grid: Grid) -> str:
    """Return a human-readable grid with 3x3 separators; 0 shows as '.'."""
    lines = []
    for r in range(9):
        row_tokens = []
        for c in range(9):
            v = grid[r][c]
            row_tokens.append(str(v) if v != 0 else '.')
            if c in {2, 5}:
                row_tokens.append("|")
        lines.append(" ".join(row_tokens))
        if r in {2, 5}:
            lines.append("-" * 21)
    return "\n".join(lines)


def print_grid(grid: Grid) -> None:
    print(format_grid(grid))


def is_grid_complete(grid: Grid) -> bool:
    return all(all(cell != 0 for cell in row) for row in grid)


def copy_grid(grid: Grid) -> Grid:
    return [row[:] for row in grid]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Parse and pretty-print a Sudoku file.")
    parser.add_argument("file", help="Path to the Sudoku .txt file")
    args = parser.parse_args()

    g = parse_sudoku_file(args.file)
    print_grid(g)