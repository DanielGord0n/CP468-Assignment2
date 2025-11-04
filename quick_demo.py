"""
=============================================================================
QUICK DEMO RUNNER - For LIVE DEMO
=============================================================================
"""

# Change these values to match the puzzle given
CUSTOM_PUZZLE = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],
    
    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],
    
    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9]
]

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from person_a.csp_model import SudokuCSP
from person_b.ac3 import ac3
from person_c.input_parser import print_grid, is_grid_complete
from person_d.solver_extension import backtracking_search


def print_separator(char="=", length=70):
    print("\n" + char * length)


def run_demo(puzzle):
    """Run the complete Sudoku solving demo."""
    
    print_separator()
    print("  SUDOKU SOLVER - LIVE DEMO")
    print("  CP468 Assignment 2 - Group Presentation")
    print_separator()
    
    # Step 1: Show Input
    print("\n[STEP 1] INPUT PUZZLE")
    print("-" * 70)
    print_grid(puzzle)
    filled = sum(1 for row in puzzle for cell in row if cell != 0)
    print(f"\nGiven clues: {filled}/81 cells")
    
    # Step 2: Create CSP
    print("\n[STEP 2] CSP MODEL (Person A - Daniel)")
    print("-" * 70)
    csp = SudokuCSP(puzzle)
    print(f"Created CSP with {len(csp.variables)} variables")
    print(f"Generated {len(csp.constraints)//2} constraint pairs")
    
    # Step 3: AC-3
    print("\n[STEP 3] AC-3 ALGORITHM (Person B - Sam)")
    print("-" * 70)
    print("Running AC-3 to enforce arc consistency...")
    is_consistent, is_solved, queue_log = ac3(csp)
    
    print(f"\nAC-3 completed in {len(queue_log)} iterations")
    print(f"CSP is consistent: {is_consistent}")
    print(f"Fully solved by AC-3: {is_solved}")
    
    if not is_consistent:
        print("\nPUZZLE IS INCONSISTENT - No solution exists")
        return
    
    # Show AC-3 statistics
    queue_lengths = [e["remaining_queue_length"] for e in queue_log]
    print(f"\nQueue statistics:")
    print(f"  - Max queue length: {max(queue_lengths)}")
    print(f"  - Avg queue length: {sum(queue_lengths)/len(queue_lengths):.1f}")
    
    print("\nPuzzle after AC-3:")
    print_grid(csp.get_puzzle())
    
    # Step 4: Backtracking (if needed)
    print("\n[STEP 4] BACKTRACKING SEARCH (Person D - Samit)")
    print("-" * 70)
    
    if not is_solved:
        print("AC-3 didn't fully solve it. Running backtracking with MRV...")
        success, stats = backtracking_search(csp)
        
        if success:
            print(f"\nBacktracking successful")
            print(f"  - Assignments made: {stats['assignment_count']}")
            print(f"  - Backtracks: {stats['backtrack_count']}")
        else:
            print("\nBacktracking failed")
            return
    else:
        print("Puzzle fully solved by AC-3 alone - No backtracking needed")
    
    # Step 5: Final Solution
    print("\n[STEP 5] FINAL SOLUTION")
    print("-" * 70)
    final = csp.get_puzzle()
    
    if is_grid_complete(final):
        print("\n*** SOLUTION FOUND ***\n")
        print_grid(final)
        print_separator()
        print("  PUZZLE SOLVED SUCCESSFULLY")
        print_separator()
    else:
        print("\nSolution incomplete")
        print_grid(final)


if __name__ == "__main__":
    print("\n" * 2)
    run_demo(CUSTOM_PUZZLE)
    print("\n" * 2)
