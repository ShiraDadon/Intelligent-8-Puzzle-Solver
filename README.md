# Intelligent 8-Puzzle Solver

An AI-based solver for the classic 8-puzzle problem, developed as part of an Artificial Intelligence course.

The project implements and compares two search algorithms:

- **Breadth-First Search (BFS)**
- **A\* Search** using Manhattan distance with linear conflict heuristic

## Problem Description

The 8-puzzle is a sliding-tile puzzle played on a 3x3 board.  
The board contains 8 numbered tiles and one blank space.

The goal is to move the tiles, one step at a time, until the board reaches the goal configuration:

```text
0 1 2
3 4 5
6 7 8
```

In this project, the blank tile is represented by `0`.

Each move slides one tile into the blank space.  
For the output, the program prints the tile number that moved.

## Board Representation

Each puzzle state is represented as a list of 9 integers.

For example:

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

### Breadth-First Search (BFS)

**BFS** is an uninformed search algorithm that expands states level by level.

Because every move has the same cost, **BFS** guarantees an optimal solution in terms of the minimum number of moves.  
However, it may expand many states and require more memory.

### A\* Search

**A\*** is an informed search algorithm that prioritizes states using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` is the actual cost from the initial state to the current state.
- `h(n)` is the estimated cost from the current state to the goal.

In this project, **A\*** uses:

```text
Manhattan distance + 2 * number of linear conflicts
```

This heuristic helps guide the search toward the goal and usually expands fewer states than **BFS**.

## Heuristic

The heuristic combines two parts:

### Manhattan Distance

Manhattan distance calculates how far each numbered tile is from its goal position by rows and columns.  
The blank tile `0` is ignored.

### Linear Conflict

A linear conflict occurs when two tiles are already in their correct goal row or column, but appear in the wrong relative order.

In that case, at least one of them must move out of the row or column and later return.  
Therefore, each conflict adds two extra moves to the heuristic estimate.

## Implementation Details

The project is divided into several modules:

- `Tiles.py` - program entry point, input validation, algorithm execution, and output printing.
- `node.py` - represents a puzzle state, including the board, parent state, path cost, and moved tile.
- `state_space.py` - creates the initial and goal states and generates legal neighbor states.
- `transition_model.py` - applies a move and creates the next state.
- `bfs.py` - implements Breadth-First Search.
- `a_star.py` - implements A\* Search.
- `heuristic.py` - implements Manhattan distance with linear conflict.
- `priority_queue.py` - manages the A\* frontier using a heap.
- `action.py`, `cost_func.py`, `constants.py` - supporting classes and constants.

The main supporting structures are:

- a queue for **BFS**
- a heap-based priority queue for **A\***
- a set of expanded states to avoid repeated expansions

## How to Run

From the project folder, run:

```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

The program receives exactly 9 numbers separated by spaces.

The input must contain each number from `0` to `8` exactly once.

## Output

For each algorithm, the program prints:

- Algorithm name
- Path of moved tiles
- Path length
- Number of expanded states

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
