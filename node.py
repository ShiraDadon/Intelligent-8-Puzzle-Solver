"""
Defines a puzzle-state node and helpers for board representation and path output.
"""

from constants import BOARD_SIZE, BOARD_SIDE


class Node:
    def __init__(
        self,
        tiles,
        is_initial=False,
        is_goal=False,
        parent_node=None,
        action_from_parent=None,
        path_cost=0,
        moved_tile_number=None,
    ):
        self.parent_node = parent_node
        self.action_from_parent = action_from_parent
        self.path_cost = path_cost
        self.is_initial = is_initial
        self.is_goal = is_goal
        self.moved_tile_number = moved_tile_number
        self.tiles = tiles
        self.board_matrix = []

    def __hash__(self):
        # A node is identified by its board arrangement, so it can be stored in sets and dictionaries.
        return hash(tuple(self.tiles))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.tiles == other.tiles

    def build_board_matrix(self):
        """Build a 3x3 matrix representation only when it is needed."""
        self.board_matrix.clear()
        for start_index in range(0, BOARD_SIZE, BOARD_SIDE):
            self.board_matrix.append(self.tiles[start_index:start_index + BOARD_SIDE])

    def print_board(self):
        """Print the board in 3x3 format. Used mainly for local debugging."""
        if not self.board_matrix:
            self.build_board_matrix()
        for board_row in self.board_matrix:
            print(board_row)
        print()

    def print_moved_tile(self):
        """Print the tile that moved into the blank position to create this node."""
        if self.moved_tile_number is not None:
            print(self.moved_tile_number, end=' ')

    def find_blank_tile_position(self):
        """Return the row and column of the blank tile, represented by 0."""
        for tile_index in range(BOARD_SIZE):
            if self.tiles[tile_index] == 0:
                row = tile_index // BOARD_SIDE
                column = tile_index % BOARD_SIDE
                return row, column
        return None

    def swap_tiles_by_position(self, row1, column1, row2, column2):
        first_index = row1 * BOARD_SIDE + column1
        second_index = row2 * BOARD_SIDE + column2
        self.tiles[first_index], self.tiles[second_index] = self.tiles[second_index], self.tiles[first_index]

    def get_path_cost(self):
        return self.path_cost

    def set_moved_tile(self, moved_tile_number):
        self.moved_tile_number = moved_tile_number

    def get_parent_node(self):
        return self.parent_node

    def get_tiles(self):
        return self.tiles

    def get_action_from_parent(self):
        return self.action_from_parent

    def get_board_matrix(self):
        if not self.board_matrix:
            self.build_board_matrix()
        return self.board_matrix
