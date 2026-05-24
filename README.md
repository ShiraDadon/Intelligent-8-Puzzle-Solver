# Intelligent 8-Puzzle Solver

This project is a Python-based implementation of the classic 8-puzzle problem, developed as part of an Artificial Intelligence course.

## Overview

The 8-puzzle is a sliding-tile puzzle played on a 3x3 board with 8 numbered tiles and one blank space.  
The goal is to reach the target configuration by sliding tiles into the blank space.

In this project, the blank tile is represented by `0`, and each puzzle state is represented as a list of 9 numbers.

Goal state:

```text
0 1 2
3 4 5
6 7 8
```

The project implements and compares two search algorithms:

- **Breadth-First Search (BFS)**
- **A* Search** with Manhattan distance and linear conflict heuristic

The program evaluates each algorithm by printing the solution path, path length, and number of expanded nodes.

## Features

- Solves the 8-puzzle problem for valid 3x3 board configurations.
- Implements both uninformed and informed AI search algorithms.
- Uses efficient structures such as queues, sets, and a heap-based priority queue.
- Includes input validation to ensure the board contains exactly the numbers `0` to `8`.
- Outputs the moved tiles, solution length, and expanded node count for each algorithm.

## Algorithms

### Breadth-First Search (BFS)

BFS expands states level by level.  
Since every move has the same cost, BFS guarantees an optimal solution in terms of the minimum number of moves.

### A* Search

A* prioritizes states using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the actual cost from the initial state to the current state.
- `h(n)` is the estimated cost from the current state to the goal.

The heuristic used in this project combines:

```text
Manhattan distance + 2 * linear conflicts
```

Manhattan distance estimates how far each tile is from its goal position.  
Linear conflict improves the estimate by detecting tiles that are in the correct row or column but block each other because they appear in the wrong order.

## Usage

### Requirements

- Python 3.x
- Standard Python libraries only

### Run the Program

From the project folder, run:

```bash
python Tiles.py num1 num2 num3 num4 num5 num6 num7 num8 num9
```

Replace `num1` to `num9` with unique numbers from `0` to `8`.

### Example

```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

## Output

For each algorithm, the program prints:

- Algorithm name
- Path of moved tiles
- Path length
- Number of expanded nodes

Example format:

```text
Algorithm:  BFS
Path :  ...
Path length:  ...
Expanded:  ...

Algorithm:  A*
Path :  ...
Path length:  ...
Expanded:  ...
```

## File Structure

- `Tiles.py` - main program entry point, input validation, algorithm execution, and output printing.
- `bfs.py` - implementation of Breadth-First Search.
- `a_star.py` - implementation of A* Search.
- `heuristic.py` - Manhattan distance and linear conflict heuristic.
- `node.py` - representation of a puzzle state.
- `state_space.py` - creation of states and generation of valid neighbors.
- `transition_model.py` - logic for applying moves and creating successor states.
- `priority_queue.py` - heap-based priority queue used by A*.
- `action.py`, `cost_func.py`, `constants.py` - supporting classes and constants.

## Skills Demonstrated

- AI search algorithms
- Heuristic function design
- State-space representation
- Data structures: queues, sets, and priority queues
- Clean modular Python implementation
