"""
Shared constants for the 8-puzzle project.
"""

import math

# The 8-puzzle board is represented as a flat list of 9 tiles.
# BOARD_SIDE is used whenever the list index needs to be converted to row/column coordinates.
BOARD_SIZE = 9
BOARD_SIDE = int(math.sqrt(BOARD_SIZE))

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
ACTIONS = [UP, DOWN, LEFT, RIGHT]

# 0 represents the blank tile.
GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]

BF_SEARCH = "BFS"
A_STAR = "A*"
