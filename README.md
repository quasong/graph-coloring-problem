# Graph Coloring Problem

This repository, graph-coloring-problem, focuses on implementing and studying a collection of algorithms to address the
Graph Coloring Problem. The Graph Coloring Problem is a classic and computationally challenging problem in computer
science and combinatorics, where we aim to assign colors to the vertices of a graph such that no two adjacent vertices
share the same color.

## Getting Started

This project requires Python interpreter version 3.5 or above.
To run the project, execute the following command:

```zsh
python main.py
```
or
```zsh
python3 main.py
```

## Algorithms & Techniques

In our approach to solving the Graph Coloring Problem, we have implemented a variety of algorithms, each with its unique
strengths, which include:

### Backtracking

Backtracking is a fundamental technique used in graph coloring algorithms to systematically
explore and search for solutions in a problem space. It involves a depth-first search traversal
of the search tree, making assignments to variables and backtracking when a constraint violation
occurs.

In regular backtracking, the algorithm assigns values to variables one at a time, exploring the
search space until a valid solution is found or all possibilities have been exhausted. When a
variable assignment leads to a constraint violation, the algorithm backtracks to the previous
assignment and explores alternative options.

#### Conflict-Directed Backjumping ⚠️

Conflict-Directed Backjumping (CDB) is an optimization technique applied during backtracking.
It aims to improve efficiency by identifying and avoiding unnecessary search paths. CDB uses
conflict information to determine which variables and assignments are responsible for the
conflicts and "jumps" directly to a higher-level variable that may have caused the conflict,
skipping intermediate search states.

### Heuristic Ordering

Heuristic ordering techniques are employed in graph coloring algorithms to determine the order
in which variables are assigned values. They aim to improve efficiency by selecting variables
that are likely to result in successful assignments or provide valuable information during the
search process.

#### Minimum Remaining Values

Minimum Remaining Values (MRV) is a heuristic that selects the variable with the fewest
remaining legal values. It prioritizes variables that have the least number of options,
potentially reducing the branching factor and the search space.

`Optimization ⚠️` Randomly choice a variable from the sorted variables to avoid the search process getting
trapped in local optima.

#### Least Constraining Value

Least Constraining Value (LCV) is a heuristic that selects the value that rules out the fewest
choices for neighboring variables. It considers the impact of each value on the constraints of
neighboring variables, preferring values that allow for greater flexibility in subsequent
assignments.

`Optimization ⚠️` Filter the sorted values and return those values which have fewer or equal
constraints than the average.

#### Degree Heuristic

Degree Heuristic (DH) is a heuristic that selects the variable with the largest degree, i.e.,
the variable connected to the most other variables in the graph. It prioritizes variables that
have a higher degree of interaction with other variables, potentially leading to earlier
constraint propagation and more informed decisions.

### Constraint Propagation

Constraint propagation is a technique used in graph coloring algorithms to enforce consistency
among the variables and their domains. It aims to reduce the search space by eliminating invalid
assignments based on the constraints of the problem.

#### Forward Checking

Forward checking is a local consistency technique that updates the domains of unassigned variables
after assigning a value to a variable. It removes inconsistent values from neighboring variables'
domains, pruning options that violate constraints.

#### Arc Consistency

Arc consistency, also known as AC-3, is a more global consistency technique. It ensures that
every value in a variable's domain is consistent with all its neighbors. It iteratively checks
and removes values that cannot satisfy the constraints, propagating these constraints through
the graph.

#### Path Consistency

Path consistency is a stronger form of consistency than arc consistency. It extends the idea of
arc consistency by considering longer paths in the graph. It enforces consistency along all
possible paths between variables, ensuring that no values violate the constraints.

### Value Symmetry

In graph coloring algorithms, the "value symmetry" technique refers to a strategy that exploits
symmetry in the assignment of values to variables. It aims to reduce redundancy and improve the
efficiency of the algorithm. Value symmetry arises when there are multiple equivalent assignments of values to variables
that result in the same overall solution. The value symmetry technique leverages this property
by eliminating redundant search paths and avoiding unnecessary computations.

## Test

| file          | min colors | techniques enable | best scenario time | backtracking |
|---------------|------------|-------------------|--------------------|--------------|
| le450_5a.col  | 5 ✅        | -                 | 0.2s               | 101          |
| le450_5b.col  | 5 ✅        | -                 | 0.1s               | 4            |
| le450_5c.col  | 5 ✅        | -                 | 0.1s               | 6            |
| le450_5d.col  | 5 ✅        | -                 | 0.1s               | 0            |
| le450_15a.col | 15 ✅       | rfj               | 1.99hrs            | 14265710     |
| le450_15b.col | 15 ✅       | rfj               | 0.1s               | 0            |
| le450_15c.col | 22         | rfj               | 3.9s               | 3971         |
| le450_15d.col | 23         | rfj               | 0.8s               | 663          |
| le450_25a.col | 25 ✅       | -                 | 0.2s               | 0            |
| le450_25b.col | 25 ✅       | -                 | 0.2s               | 0            |
| le450_25c.col | 27         | j                 | 2.0s               | 1422         |
| le450_25d.col | 27         | rfj               | 12.0s              | 12478        |

## Usage

Please refer to the individual documentation for each algorithm within the repository for specific usage and
implementation details.

This project serves as a comprehensive resource for anyone interested in the Graph Coloring Problem, providing a robust
set of strategies to tackle this intriguing problem. It is also a valuable tool for comparative analysis of different
algorithms under various problem configurations.

Feel free to explore, use, and contribute to this project.
