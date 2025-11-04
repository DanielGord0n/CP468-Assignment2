# Person D - Search Algorithm Developer

## Responsibilities

- Implement backtracking search algorithm to solve puzzles not fully resolved by AC-3
- Apply Minimum Remaining Values (MRV) heuristic for efficient variable selection
- Use forward checking to reduce search space
- Integrate with AC-3 output to leverage reduced domains
- Track search statistics (assignments, backtracks) for analysis
- Ensure final output distinguishes between AC-3-only and backtracking solutions

## Deliverables

- `solver_extension.py`
- Report section: Additional Algorithm Implementation (Backtracking with MRV)

## Marks Allocation

Part IV - Additional Algorithm Implementation: **20 marks**

## Algorithm Overview

**Backtracking Search**: Systematic depth-first search that assigns values to variables and backtracks when conflicts arise.

**MRV Heuristic**: Selects the unassigned variable with the smallest domain size, reducing branching factor.

**Forward Checking**: After each assignment, removes conflicting values from neighboring variables' domains.

## Usage for Integration

```python
from person_a.csp_model import SudokuCSP
from person_b.ac3 import ac3
from person_d.solver_extension import backtracking_search, print_search_stats

# Create CSP and apply AC-3
csp = SudokuCSP(puzzle)
is_consistent, is_solved, queue_log = ac3(csp)

# If AC-3 doesn't solve it, apply backtracking
if is_consistent and not is_solved:
    success, stats = backtracking_search(csp)
    print_search_stats(stats)
```

## Integration Points

- Works with `SudokuCSP` from person_a
- Uses domains reduced by `ac3()` from person_b
- Maintains same logging and statistics pattern as other modules
