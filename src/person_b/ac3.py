"""
Person B - AC-3 Algorithm Developer
-------------------------------------------------------------

Impliments the AC-3 algorithm for enforcing arc consistency on
the Sudoku CSP

Integration:
    - Works directly with the SudokuCSP class defined in src/person_a/csp_model.py.
    - Uses SudokuCSP.domains, SudokuCSP.constraints, and SudokuCSP.get_neighbors().

Outputs:
    - Enforces arc consistency by pruning domains.
    - Logs queue length at every iteration for later visualization (Person C).
    - Returns whether the CSP is consistent and whether a complete Sudoku solution was found.

Deliverables:
    - ac3.py

Author: Sam Oreskovic (Person B)
Course: CP468 - Artificial Intelligence
Assignment 2
"""

from collections import deque

def ac3(csp):
    """
    Enforce arc consistency on the given CSP.

    Parameters: @ csp - Given CSP Instance

    Returns: @ (is_consistent, is_solved, queue_log)
    """
    # Initialize queue given arcs from constraints
    queue = deque(csp.constraints)
    queue_log = []

    # Process queue until arcs consistent
    while queue:
        (Xi, Xj) = queue.popleft()

        # Log current queue state prior to revising
        queue_log.append({
            "processing_arc": (Xi, Xj),
            "remaining_queue_length": len(queue),
            "domain_sizes": {v: len(csp.domains[v]) for v in csp.variables}
        })


        # Revise Xi's domain to be consistent with Xj
        if revise(csp, Xi, Xj):
            # If Xi's domain becomes empty, inconsistent CSP
            if len(csp.domains[Xi]) == 0:
                return False, False, queue_log
            
            # Add arcs (Xk, Xi) for all neighbors Xk except for Xj
            for Xk in csp.get_neighbors(Xi):
                if Xk != Xj:
                    queue.append((Xk, Xj))
    
    is_solved = csp.is_solved()
    return True, is_solved, queue_log



def revise(csp, Xi, Xj):
    """
    Revise the domain of variable Xi to maintain consistency with Xj.

    Parameters: @ csp - Given CSP Instance
                @ Xi - int - Index of variable to be revised
                @ Xj - int - Index of neighboring variable providing constraint

    Returns: @ Bool - True if Xi's domain was reduced, otherwise False.
    """
    revised = False
    to_remove = set()

    for x in csp.domains[Xi]:
        # Iterate over a copy
        for x in list(csp.domains[Xi]):
            if not any(is_constraint_satisfied(Xi, x, Xj, y) for y in csp.domains[Xj]):
                to_remove.add(x)

        # Safely update the domain
        if to_remove:
            csp.domains[Xi] = csp.domains[Xi] - to_remove
            revised = True

    
    return revised



def is_constraint_satisfied(Xi, x, Xj, y):
    """
    Constraint checker for Sudoku:
    Two variables confict if they share a row, column, or 3x3 block AND have equal values.

    Parameters: @ Xi, Xj - int - Variable indices (0-80)
                @ x, y - int - Proposed values for Xi and Xj respectively.

    Returns: @ Bool - True if assignment (Xi = x, Xj = y), does NOT violate the previous constraints, 
                otherwise False.
    """
    # Same value cannot occur if variables are related
    if x == y:
        # Compute row, col for each variable
        row_i, col_i = divmod(Xi, 9)
        row_j, col_j = divmod(Xj, 9)

        same_row = row_i == row_j
        same_col = col_i == col_j
        same_block = (row_i // 3 == row_j // 3) and (col_i // 3 == col_j // 3)

        if same_row or same_col or same_block:
            return False
        
    return True



def print_queue_log(queue_log, limit=10):
    """
    Utility function: print the first few entries of the queue log for inspection.
    """
    print(f"\nAC-3 Queue Log (showing first {limit} steps):")
    print("-" * 40)
    
    # iterate over entries and print them
    for i, entry in enumerate(queue_log[:limit]):
        arc = entry["processing_arc"]
        length = entry["remaining_queue_length"]
        print(f"Step {i + 1:02d}: Processing arc {arc}, Remaining queue length = {length}")

    print("-" * 40)
