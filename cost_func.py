"""
Defines the uniform step-cost function used by the search algorithms.
"""

class CostFunction:
    def calculate_step_cost(self, current_node, action_from_parent, next_node):
        """Return the cost of one move. In this puzzle, every move costs exactly 1."""
        return 1
