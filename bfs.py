"""
Breadth-First Search implementation for the 8-puzzle problem.
"""

from constants import BF_SEARCH


class BFS:
    def __init__(self, state_space, start_node):
        self.algorithm_name = BF_SEARCH
        self.state_space = state_space
        self.start_node = start_node
        self.moved_tiles_path = []
        self.expanded_nodes = set()
        self.frontier_queue = []

    def find_solution(self):
        """Run Breadth-First Search and return the goal node if a solution is found."""
        self.frontier_queue.append(self.start_node)

        while self.frontier_queue:
            current_node = self.frontier_queue.pop(0)

            if current_node in self.expanded_nodes:
                continue

            # BFS expands nodes by depth, so with unit costs the first solution found is shortest.
            self.expanded_nodes.add(current_node)

            if self.state_space.is_goal_node(current_node):
                self.build_moved_tiles_path(current_node)
                return current_node

            neighbor_nodes = self.state_space.generate_neighbors(current_node)
            self.frontier_queue.extend(neighbor_nodes)

        return None

    def build_moved_tiles_path(self, goal_node):
        """Build the ordered list of moved tiles from the start node to the goal node."""
        current_node = goal_node
        while current_node.get_parent_node() is not None:
            self.moved_tiles_path.insert(0, current_node.moved_tile_number)
            current_node = current_node.get_parent_node()

    def get_solution_path_nodes(self, final_node):
        """Return all nodes from the start node to the final node."""
        current_node = final_node
        solution_path = []
        while current_node is not None:
            solution_path.insert(0, current_node)
            current_node = current_node.get_parent_node()
        return solution_path

    def get_expanded_nodes_count(self):
        return len(self.expanded_nodes)

    def get_algorithm_name(self):
        return self.algorithm_name
