# Intelligent 8-Puzzle Solver

An AI-based solver for the classic 8-puzzle problem, developed as part of an Artificial Intelligence course.

The project implements and compares two search algorithms:

- Breadth-First Search (BFS)
- A* Search using Manhattan distance with linear conflict heuristic

## Problem Description

The 8-puzzle is a sliding-tile puzzle played on a 3x3 board.  
The board contains 8 numbered tiles and one blank space.

The goal is to move the tiles, one step at a time, until the board reaches the goal configuration:

```text
0 1 2
3 4 5
6 7 8
```

In this implementation, the blank tile is represented by `0`.

A valid move is performed by moving the blank tile:

- Up
- Down
- Left
- Right

For the output, the program prints the tile number that moved into the blank space.

## Board Representation

Each puzzle state is represented as a list of 9 integers.

Example:

```text
1 4 0 5 8 2 3 6 7
```

represents the board:

```text
1 4 0
5 8 2
3 6 7
```

## Search Algorithms

### Breadth-First Search - BFS

BFS is an uninformed search algorithm.  
It expands states level by level, meaning it first checks all states that can be reached in one move, then all states that can be reached in two moves, and so on.

Since every move has the same cost, BFS guarantees finding an optimal solution in terms of the minimum number of moves.

However, BFS may expand many nodes and can be expensive in both time and memory.

### A* Search

A* is an informed search algorithm.  
It uses both the actual cost from the start state and an estimated cost to the goal state.

A* evaluates each node using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the actual cost from the initial state to the current node.
- `h(n)` is the heuristic estimate from the current node to the goal.

In this project, A* uses a heuristic based on:

```text
Manhattan distance + 2 * number of linear conflicts
```

This helps A* expand fewer nodes than BFS while still finding an optimal solution when the heuristic is admissible and consistent.

## Heuristic Used by A*

### Manhattan Distance

Manhattan distance measures how far each numbered tile is from its goal position.

For each tile, the algorithm calculates:

```text
row distance + column distance
```

The blank tile `0` is ignored.

For example, if a tile is one row away and two columns away from its goal position, its Manhattan distance is `3`.

### Linear Conflict

A linear conflict occurs when two tiles are already in their correct goal row or correct goal column, but they are in the wrong relative order.

In this case, Manhattan distance alone is too optimistic, because at least one of the tiles must move out of that row or column and later return to it.

Each linear conflict adds at least two extra moves, so the heuristic adds:

```text
2 * number of linear conflicts
```

This makes the heuristic more informative than Manhattan distance alone.

## Main Data Structures

- `Node` - represents a puzzle state, including the board, parent node, path cost, action from parent, and moved tile.
- `PriorityQueue` - used by A* to select the node with the lowest `f(n)` value.
- `set` - used to store expanded states and avoid expanding the same state more than once.
- `list` - used to represent the board and to manage the BFS frontier.

## Main Components

- `Tiles.py` - program entry point, input parsing, validation, algorithm execution, and output printing.
- `node.py` / `Node` - represents a single puzzle state.
- `state_space.py` / `StateSpace` - creates initial and goal states, checks goal states, and generates neighbors.
- `transition_model.py` / `TransitionModel` - applies legal moves and creates successor states.
- `action.py` / `Action` - represents a move direction and its cost.
- `cost_func.py` / `CostFunction` - defines the step cost. In this project, every move costs `1`.
- `bfs.py` / `BFS` - implements Breadth-First Search.
- `a_star.py` / `AStar` - implements A* Search.
- `heuristic.py` / `Heuristic` - implements Manhattan distance with linear conflict.
- `priority_queue.py` / `PriorityQueue` - manages the A* frontier efficiently.
- `constants.py` - stores constants such as board size, directions, and goal state.

## How to Run

From the project folder, run:

```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

The program receives exactly 9 numbers separated by spaces.

The numbers must be:

```text
0 1 2 3 4 5 6 7 8
```

without duplicates.

## Output

For each algorithm, the program prints:

- Algorithm name
- Path of moved tiles
- Path length
- Number of expanded nodes

Example output format:

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

## Purpose

The purpose of this project is to demonstrate classic AI search techniques on a well-known state-space search problem.

The project compares uninformed search using BFS with informed search using A*, and shows how a stronger heuristic can reduce the number of expanded states.
