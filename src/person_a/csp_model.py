"""
CSP Model for 9x9 Sudoku Puzzle

Variables: 81 cells indexed 0-80
Domains: Values 1-9 for each cell
Constraints: Binary constraints between cells in same row, column, or 3x3 subgrid
"""

class SudokuCSP:
    
    def __init__(self, puzzle):
        """
        Initialize CSP from 9x9 puzzle (0 = empty cell).
        """
        self.variables = list(range(81))
        
        # Initialize domains
        self.domains = {}
        for i in range(81):
            row, col = i // 9, i % 9
            if puzzle[row][col] == 0:
                self.domains[i] = set(range(1, 10))
            else:
                self.domains[i] = {puzzle[row][col]}
        
        # Build constraints
        self.constraints = self._build_constraints()
    
    def _build_constraints(self):
        """Build binary constraints (row, column, subgrid)."""
        constraints = set()
        
        # Row constraints
        for row in range(9):
            for col1 in range(9):
                for col2 in range(col1 + 1, 9):
                    var1, var2 = row * 9 + col1, row * 9 + col2
                    constraints.add((var1, var2))
                    constraints.add((var2, var1))
        
        # Column constraints
        for col in range(9):
            for row1 in range(9):
                for row2 in range(row1 + 1, 9):
                    var1, var2 = row1 * 9 + col, row2 * 9 + col
                    constraints.add((var1, var2))
                    constraints.add((var2, var1))
        
        # Subgrid constraints
        for box_row in range(3):
            for box_col in range(3):
                cells = [
                    (box_row * 3 + r) * 9 + (box_col * 3 + c)
                    for r in range(3) for c in range(3)
                ]
                for i, var1 in enumerate(cells):
                    for var2 in cells[i + 1:]:
                        constraints.add((var1, var2))
                        constraints.add((var2, var1))
        
        return constraints
    
    def get_neighbors(self, var):
        """Get all neighbors of a variable."""
        return {v2 for v1, v2 in self.constraints if v1 == var}
    
    def is_solved(self):
        """Check if puzzle is solved."""
        return all(len(self.domains[var]) == 1 for var in self.variables)
    
    def get_puzzle(self):
        """Convert to 9x9 list (0 for unsolved cells)."""
        puzzle = [[0] * 9 for _ in range(9)]
        for var in self.variables:
            row, col = var // 9, var % 9
            if len(self.domains[var]) == 1:
                puzzle[row][col] = list(self.domains[var])[0]
        return puzzle
