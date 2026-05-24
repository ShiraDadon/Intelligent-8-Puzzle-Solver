"""
Applies puzzle moves to nodes and creates successor states.
"""

from constants import BOARD_SIDE, UP, DOWN, LEFT, RIGHT
from node import Node


class TransitionModel:
    def create_successor_node(self, current_node, action):
        """Create the next node after moving the blank tile in the requested direction."""
        blank_row, blank_column = current_node.find_blank_tile_position()
        next_blank_row, next_blank_column = blank_row, blank_column
        move_direction = action.get_move_direction()

        if move_direction == UP:
            next_blank_row = blank_row - 1
        elif move_direction == DOWN:
            next_blank_row = blank_row + 1
        elif move_direction == LEFT:
            next_blank_column = blank_column - 1
        elif move_direction == RIGHT:
            next_blank_column = blank_column + 1

        if not (0 <= next_blank_row < BOARD_SIDE and 0 <= next_blank_column < BOARD_SIDE):
            return None

        successor_node = Node(
            current_node.get_tiles().copy(),
            parent_node=current_node,
            action_from_parent=action,
            path_cost=current_node.get_path_cost() + 1,
        )
        successor_node.swap_tiles_by_position(blank_row, blank_column, next_blank_row, next_blank_column)

        # The action moves the blank tile, but the required output is the tile number that moved into it.
        moved_tile_number = successor_node.get_tiles()[blank_row * BOARD_SIDE + blank_column]
        successor_node.set_moved_tile(moved_tile_number)
        return successor_node
