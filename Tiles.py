"""
Command-line entry point: reads input, runs BFS and A*, and prints results.
"""

import argparse

from a_star import AStar
from bfs import BFS
from cost_func import CostFunction
from heuristic import Heuristic
from state_space import StateSpace


def parse_tiles_from_command_line():
    parser = argparse.ArgumentParser(description="Solve the 8-puzzle problem.")
    parser.add_argument(
        'tiles',
        metavar='T',
        type=int,
        nargs='+',
        help='the initial order of the tiles, separated by spaces',
    )
    parsed_arguments = parser.parse_args()
    return parsed_arguments.tiles


def validate_tiles_list(initial_tiles):
    """Validate that the input contains each tile number from 0 to 8 exactly once."""
    if len(initial_tiles) != 9:
        raise ValueError("Number of tiles must be 9")

    for tile_value in initial_tiles:
        if tile_value < 0 or tile_value > 8:
            raise ValueError("Tiles must be numbers from 0 to 8")

    unique_tiles = set(initial_tiles)
    if len(unique_tiles) != 9:
        raise ValueError("Tiles must not contain duplicates")

    return True


def print_algorithm_result(search_algorithm, final_node):
    print("Algorithm: ", search_algorithm.get_algorithm_name())
    print("Path : ", end=' ')

    if final_node is None:
        print("No solution found.", end='')
    else:
        solution_path_nodes = search_algorithm.get_solution_path_nodes(final_node)
        for solution_node in solution_path_nodes:
            solution_node.print_moved_tile()

    print()
    print("Path length: ", len(search_algorithm.moved_tiles_path))
    print("Expanded: ", search_algorithm.get_expanded_nodes_count())


if __name__ == "__main__":
    initial_tiles = parse_tiles_from_command_line()
    # initial_tiles = [2, 3, 6, 8, 7, 1, 5, 0, 4]  # Example input: no solution found
    # initial_tiles = [2, 0, 6, 8, 7, 1, 5, 3, 4]  # Example input: has solution
    # initial_tiles = [1, 0, 2, 3, 7, 8, 6, 4, 5]  # Example input: 15 steps

    try:
        if validate_tiles_list(initial_tiles):
            state_space = StateSpace()
            start_node = state_space.create_initial_state(initial_tiles)
            goal_node = state_space.create_goal_state()

            bfs_solver = BFS(state_space, start_node)
            bfs_goal_node = bfs_solver.find_solution()
            print_algorithm_result(bfs_solver, bfs_goal_node)

            print()

            heuristic = Heuristic(goal_node)
            cost_function = CostFunction()
            a_star_solver = AStar(
                state_space,
                start_node,
                heuristic.estimate_manhattan_with_linear_conflict,
                cost_function,
            )
            a_star_goal_node = a_star_solver.find_solution()
            print_algorithm_result(a_star_solver, a_star_goal_node)

    except ValueError as error:
        print(f"ERROR: Invalid list of tiles : {error}")
        exit()
