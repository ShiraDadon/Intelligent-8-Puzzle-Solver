"""
A* search implementation using a heuristic estimate and step-cost function.
"""

from constants import A_STAR
from priority_queue import PriorityQueue


class AStar:
    def __init__(self, state_space, start_node, heuristic_function, cost_function):
        self.algorithm_name = A_STAR
        self.state_space = state_space
        self.start_node = start_node
        self.goal_node = state_space.create_goal_state()
        self.heuristic_function = heuristic_function
        self.cost_function = cost_function
        self.moved_tiles_path = []
        self.expanded_nodes = set()
        self.frontier_queue = PriorityQueue()

    def find_solution(self):
        """Run A* search and return the goal node if a solution is found."""
        start_priority = self.start_node.get_path_cost() + self.heuristic_function(self.start_node)
        self.frontier_queue.add_or_update_priority(self.start_node, start_priority)

        while not self.frontier_queue.is_empty():
            current_node = self.frontier_queue.pop_lowest_priority_item()

            if current_node in self.expanded_nodes:
                continue

            self.expanded_nodes.add(current_node)

            if self.state_space.is_goal_node(current_node):
                self.build_moved_tiles_path(current_node)
                return current_node

            for neighbor_node in self.state_space.generate_neighbors(current_node):
                if neighbor_node not in self.expanded_nodes:
                    # A* priority is f(n) = g(n) + h(n): path cost so far plus heuristic estimate.
                    path_cost_to_neighbor = (
                        current_node.get_path_cost()
                        + self.cost_function.calculate_step_cost(
                            current_node,
                            neighbor_node.get_action_from_parent(),
                            neighbor_node,
                        )
                    )
                    neighbor_priority = path_cost_to_neighbor + self.heuristic_function(neighbor_node)
                    self.frontier_queue.add_or_update_priority(neighbor_node, neighbor_priority)

        return None

    def build_moved_tiles_path(self, goal_node):
        """Build the ordered list of moved tiles from the start node to the goal node."""
        current_node = goal_node
        while current_node.get_parent_node() is not None:
            self.moved_tiles_path.insert(0, current_node.moved_tile_number)
            current_node = current_node.get_parent_node()

    def get_algorithm_name(self):
        return self.algorithm_name

    def get_expanded_nodes_count(self):
        return len(self.expanded_nodes)

    def get_solution_path_nodes(self, final_node):
        """Return all nodes from the start node to the final node."""
        current_node = final_node
        solution_path = []
        while current_node is not None:
            solution_path.insert(0, current_node)
            current_node = current_node.get_parent_node()
        return solution_path
