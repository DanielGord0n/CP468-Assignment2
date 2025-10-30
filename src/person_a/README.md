# Person A - CSP Model Designer (Daniel)

## Deliverables
- `csp_model.py` ✓

## CSP Model

**Variables**: 81 cells indexed 0-80

**Domains**: Set {1,2,3,4,5,6,7,8,9} for empty cells, singleton for pre-filled

**Constraints**: Binary constraints - cells in same row, column, or 3x3 subgrid cannot have same value

## Usage for Person B

```python
from person_a.csp_model import SudokuCSP

# Create CSP from puzzle (0 = empty cell)
csp = SudokuCSP(puzzle)

# Access components
csp.constraints        # Set of (var1, var2) tuples
csp.domains[var]       # Domain for variable
csp.get_neighbors(var) # Get neighbors
csp.is_solved()        # Check if solved
csp.get_puzzle()       # Convert back to 9x9 list
```
