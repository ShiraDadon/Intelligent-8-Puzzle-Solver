# 8-Puzzle Solver

This project solves the 8-puzzle problem using two search algorithms:

- Breadth-First Search (BFS)
- A* Search with Manhattan distance and linear conflict

The board is represented as a list of 9 numbers. The value `0` represents the blank tile.

## Main components

- `Tiles.py` - program entry point, input validation and output printing.
- `node.py` / `Node` - represents one puzzle state, including its parent node, path cost and moved tile.
- `state_space.py` / `StateSpace` - creates the initial/goal states and generates legal neighbors.
- `transition_model.py` / `TransitionModel` - applies a move to the blank tile and creates the successor node.
- `cost_func.py` / `CostFunction` - returns a cost of 1 for every move.
- `bfs.py` / `BFS` - uninformed search that expands nodes level by level.
- `a_star.py` / `AStar` - informed search that uses `g(n) + h(n)` to prioritize nodes.
- `heuristic.py` / `Heuristic` - estimates the remaining distance to the goal.
- `priority_queue.py` / `PriorityQueue` - manages the A* frontier by priority.

## Heuristic used by A*

A* chooses which node to expand according to:

`f(n) = g(n) + h(n)`

- `g(n)` is the real cost from the initial state to the current node.
- `h(n)` is the estimated remaining cost from the current node to the goal.

In this project, the heuristic is:

`Manhattan distance + 2 * number of linear conflicts`

### Manhattan distance

For every numbered tile, the algorithm checks how far the tile is from its goal position by rows and columns. The blank tile `0` is ignored.

For example, if tile `5` is one row away and two columns away from its goal position, its Manhattan distance is `3`.

### Linear conflict

A linear conflict happens when two tiles are already in their correct goal row or correct goal column, but they are in the wrong relative order.

In that situation, Manhattan distance alone is too optimistic, because at least one tile must leave the row or column and later come back. This requires at least two additional moves, so every detected conflict adds `2` to the heuristic value.

This makes the heuristic more informative than Manhattan distance alone, while still keeping it suitable for A*.

## How to run

From the project folder, run:

```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

The program receives exactly 9 numbers separated by spaces.

## Output

For each algorithm, the program prints:

- algorithm name
- path of moved tiles
- path length
- number of expanded nodes

Example format:

```text
Algorithm:  BFS
Path :  2 8 5 3 6 7 8 5 4 1
Path length:  10
Expanded:  357
```
