"""
Defines one legal move in the puzzle and its step cost.
"""

class Action:
    def __init__(self, move_direction, step_cost=1):
        self.move_direction = move_direction
        self.step_cost = step_cost

    def get_move_direction(self):
        return self.move_direction

    def get_step_cost(self):
        return self.step_cost
