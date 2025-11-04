"""
Person A - CSP Model Demo
"""

from csp_model import SudokuCSP

# Paste your puzzle here (0 = empty cell)
puzzle = [
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

def print_puzzle(puzzle):
    """Print puzzle in readable format"""
    for i, row in enumerate(puzzle):
        if i % 3 == 0 and i != 0:
            print("  " + "-" * 21)
        row_str = "  "
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += (str(val) if val != 0 else ".") + " "
        print(row_str)

print("CSP Model - Person A\n")
print("Input Puzzle:")
print_puzzle(puzzle)

# Create CSP
print("\nCreating CSP...\n")
csp = SudokuCSP(puzzle)

# Show components
print(f"Variables: {len(csp.variables)}")
print(f"Constraints: {len(csp.constraints) // 2}")
print(f"Filled cells: {sum(1 for d in csp.domains.values() if len(d) == 1)}")
print(f"Empty cells: {sum(1 for d in csp.domains.values() if len(d) > 1)}")

print(f"\nExample - Variable 0:")
print(f"  Domain: {csp.domains[0]}")
print(f"  Neighbors: {len(csp.get_neighbors(0))}")

print(f"\nSolved: {csp.is_solved()}")
