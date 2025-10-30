# CP468 - Assignment 2: Sudoku as a CSP

## Assignment Overview
This assignment involves representing Sudoku as a Constraint Satisfaction Problem (CSP) and implementing the AC-3 algorithm to enforce arc consistency.

## Requirements
- Accept Sudoku puzzles as input
- Track the AC-3 queue length at each step
- Report whether the puzzle becomes solved after enforcing arc consistency
- If not solved, apply an additional solving algorithm
- Produce readable, well-documented code and a final written report

## Project Structure

### `src/person_a/` - CSP Model Designer (Daniel)
**Marks: 20**
- CSP representation of Sudoku puzzle
- Variables, domains, and binary constraints definition

### `src/person_b/` - AC-3 Algorithm Developer
**Marks: 25**
- AC-3 algorithm implementation
- Queue tracking and arc consistency enforcement

### `src/person_c/` - Input Handler and Visual Logger
**Marks: 15**
- Sudoku puzzle input parsing
- Queue length visualization and logging

### `src/person_d/` - Search Algorithm Developer
**Marks: 20**
- Additional solving algorithm (Backtracking/MRV/Forward Checking)
- Integration with AC-3 output

### `src/person_e/` - Results and Testing Analyst
**Marks: 20 (shared)**
- Testing with various difficulty levels
- Performance analysis and results documentation

### `src/person_f/` - Documentation & Integration Lead
**Marks: 20**
- Final report compilation
- Code integration and documentation

### `results/`
- Test outputs and logs
- Performance metrics and analysis

## Marking Scheme
- Constraints handling: 20 marks
- AC-3 implementation: 25 marks
- Sudoku input format: 15 marks
- Additional implementation: 20 marks
- Code readability and documentation: 20 marks

**Total: 100 marks**

## Instructor
I. Kotsireas  
Email: ikotsire@wlu.ca

## Due Date
See course outline for submission deadline.

**Late submissions will not be accepted and will be marked with 0.**