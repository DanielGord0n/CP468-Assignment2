"""
Person D - Search Algorithm Developer (Samit)
Implements backtracking search with MRV heuristic for Sudoku solving.
"""

def backtracking_search(csp):
    stats = {'backtrack_count': 0, 'assignment_count': 0}
    success = backtrack(csp, stats)
    return success, stats


def backtrack(csp, stats):
    if csp.is_solved():
        return True
    
    # Select unassigned variable with smallest domain (MRV)
    var = select_unassigned_variable(csp)
    if var is None:
        return False
    
    # Try each value in domain
    for value in sorted(csp.domains[var]):
        if is_consistent(csp, var, value):
            # Make assignment
            saved_domains = {v: csp.domains[v].copy() for v in csp.variables}
            csp.domains[var] = {value}
            stats['assignment_count'] += 1
            
            # Recurse
            if backtrack(csp, stats):
                return True
            
            # Restore domains on failure
            csp.domains = saved_domains
            stats['backtrack_count'] += 1
    
    return False


def select_unassigned_variable(csp):
    unassigned = [var for var in csp.variables if len(csp.domains[var]) > 1]
    
    if not unassigned:
        return None
    
    return min(unassigned, key=lambda var: len(csp.domains[var]))


def is_consistent(csp, var, value):
    for neighbor in csp.get_neighbors(var):
        if len(csp.domains[neighbor]) == 1:
            if value == list(csp.domains[neighbor])[0]:
                return False
    
    return True


def print_search_stats(stats):
    """
    Utility function: print search statistics for analysis.
    
    Parameters: @ stats - Dictionary containing search metrics
    """
    print("\nBacktracking Search Statistics:")
    print("-" * 40)
    print(f"Total Assignments: {stats['assignment_count']}")
    print(f"Total Backtracks:  {stats['backtrack_count']}")
    print("-" * 40)
