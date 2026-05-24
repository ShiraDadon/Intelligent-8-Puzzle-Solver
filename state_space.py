"""
Defines the 8-puzzle state space and neighbor-generation logic.
"""

from action import Action
from constants import BOARD_SIDE, GOAL_STATE, UP, DOWN, LEFT, RIGHT
from cost_func import CostFunction
from node import Node
from transition_model import TransitionModel


class StateSpace:
    def __init__(self):
        self.transition_model = TransitionModel()
        self.cost_function = CostFunction()

    def create_initial_state(self, initial_tiles):
        return Node(initial_tiles, is_initial=True)

    def create_goal_state(self):
        return Node(GOAL_STATE, is_goal=True)

    def is_goal_node(self, node):
        return node.get_tiles() == GOAL_STATE

    def get_valid_blank_tile_moves(self, node):
        """Return only the blank-tile moves that stay inside the board limits."""
        valid_actions = []
        blank_row, blank_column = node.find_blank_tile_position()

        if blank_row > 0:
            valid_actions.append(Action(UP))
        if blank_row < BOARD_SIDE - 1:
            valid_actions.append(Action(DOWN))
        if blank_column > 0:
            valid_actions.append(Action(LEFT))
        if blank_column < BOARD_SIDE - 1:
            valid_actions.append(Action(RIGHT))

        return valid_actions

    def generate_neighbor(self, node, action):
        return self.transition_model.create_successor_node(node, action)

    def generate_neighbors(self, node):
        neighbor_nodes = []
        for action in self.get_valid_blank_tile_moves(node):
            neighbor_node = self.generate_neighbor(node, action)
            if neighbor_node is not None:
                neighbor_nodes.append(neighbor_node)
        return neighbor_nodes
