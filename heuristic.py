"""
Heuristic estimates for A*, combining Manhattan distance with linear conflict.
"""

from constants import BOARD_SIZE, BOARD_SIDE, GOAL_STATE
from node import Node


class Heuristic:
    """
    Heuristic functions used by A* to estimate how far a board state is from the goal.

    The implemented estimate is Manhattan distance with linear conflict:
        h(n) = Manhattan distance + 2 * number of linear conflicts

    Manhattan distance gives the minimum number of row/column moves each tile still needs
    if no other tiles were blocking it. Linear conflict adds a small correction for cases
    where two tiles are already in their correct goal row/column but appear in the wrong
    relative order, so one of them must move away and come back.
    """

    def __init__(self, goal_state=None):
        if goal_state is None:
            goal_state = Node(GOAL_STATE, is_goal=True)
        self.goal_state = goal_state

    def count_linear_conflict_pairs(self, state_node):
        """
        Count linear conflicts in all rows and columns of the current board.

        A row conflict exists when two tiles are located in their correct goal row,
        but the tile that should be farther left in the goal appears farther right now.
        A column conflict is the same idea, but with vertical order.

        Every such conflict requires at least two extra moves beyond the Manhattan distance:
        one tile must leave the row/column, let the other pass, and then return.
        """
        conflict_count = 0
        goal_tiles = self.goal_state.get_tiles()

        board_matrix = state_node.get_board_matrix()
        goal_matrix = self.goal_state.get_board_matrix()

        for row_index, board_row in enumerate(board_matrix):
            goal_row = goal_matrix[row_index]
            tiles_in_same_goal_row = []

            # Only tiles that belong to this exact goal row can create a row conflict.
            # We store the goal column of each such tile and then count reversed pairs.
            for tile_value in board_row:
                if tile_value != 0 and tile_value in goal_row:
                    goal_column = goal_row.index(tile_value)
                    tiles_in_same_goal_row.append((tile_value, goal_column))

            conflict_count += self.count_out_of_order_pairs(tiles_in_same_goal_row)

        for column_index in range(BOARD_SIDE):
            tiles_in_same_goal_column = []

            # Only tiles that belong to this exact goal column can create a column conflict.
            # For each such tile we store the row it should be in at the goal state.
            for board_row in board_matrix:
                tile_value = board_row[column_index]
                if tile_value != 0:
                    goal_index = goal_tiles.index(tile_value)
                    goal_column = goal_index % BOARD_SIDE

                    if goal_column == column_index:
                        goal_row = goal_index // BOARD_SIDE
                        tiles_in_same_goal_column.append((tile_value, goal_row))

            conflict_count += self.count_out_of_order_pairs(tiles_in_same_goal_column)

        return conflict_count

    def count_out_of_order_pairs(self, tiles_with_goal_positions):
        """
        Count tile pairs whose current order is reversed compared to their goal order.

        The list contains tuples of: (tile value, target position in the relevant row/column).
        If an earlier tile in the current board has a larger target position than a later tile,
        those two tiles are blocking each other.
        """
        conflict_count = 0

        for first_index in range(len(tiles_with_goal_positions)):
            for second_index in range(first_index + 1, len(tiles_with_goal_positions)):
                _, first_goal_position = tiles_with_goal_positions[first_index]
                _, second_goal_position = tiles_with_goal_positions[second_index]

                if first_goal_position > second_goal_position:
                    conflict_count += 1

        return conflict_count

    def estimate_manhattan_with_linear_conflict(self, state_node):
        """
        Estimate the remaining cost from the given state to the goal state.

        The blank tile 0 is ignored, because the required output and cost are based on
        moving numbered tiles. For every numbered tile, Manhattan distance measures the
        number of horizontal and vertical steps between its current position and its goal
        position. Then linear conflict is added to make the estimate more accurate in
        cases where tiles block each other inside their correct row or column.
        """
        state_tiles = state_node.get_tiles()
        goal_tiles = self.goal_state.get_tiles()
        total_manhattan_distance = 0

        for current_index in range(BOARD_SIZE):
            tile_value = state_tiles[current_index]

            if tile_value != 0:
                goal_index = goal_tiles.index(tile_value)

                current_row = current_index // BOARD_SIDE
                current_column = current_index % BOARD_SIDE
                goal_row = goal_index // BOARD_SIDE
                goal_column = goal_index % BOARD_SIDE

                tile_manhattan_distance = abs(current_row - goal_row) + abs(current_column - goal_column)
                total_manhattan_distance += tile_manhattan_distance

        linear_conflicts = self.count_linear_conflict_pairs(state_node)
        return total_manhattan_distance + (2 * linear_conflicts)
