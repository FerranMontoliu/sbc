from argparse import ArgumentParser
from typing import Callable, Literal

from algorithms.a import compute_a
from algorithms.csp import compute_csp
from algorithms.dijkstra import compute_dijkstra
from model.city import City
from model.connection import Connection
from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset
from utils.graph_printer import print_graph
from utils.heuristics import hf_distance, hf_duration, hf_duration_distance, hf_weighted_duration_distance


def compute(cities: [City],
            algorithm: Literal['a*', 'csp'],
            from_city: str,
            to_city: str,
            heuristic_function: Callable[[City, Connection, [City]], float | int]) -> ([City], float):
    print('Computing algorithm...')
    if algorithm == 'a*':
        path, acc_weight = compute_a(cities, from_city, to_city, heuristic_function)
    elif algorithm == 'csp':
        path, acc_weight = compute_csp(cities, from_city, to_city, heuristic_function)
    elif algorithm == 'dijkstra':
        solution = compute_dijkstra(cities, from_city, heuristic_function)
    else:
        raise Exception(f"ERROR. Invalid algorithm parameter: Must be 'a*' or 'csp', but got '{algorithm}' instead.")
    print('Search finished.')

    if path:
        print(f"The best route found is: {[c.name for c in path]}.")
        print(f"With a cost of {acc_weight}.")
    else:
        print(f"The solutions are the following: {solution}")


def parse_arguments() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('-f',
                        '--file',
                        dest='dataset_path',
                        metavar='dataset_path',
                        type=str,
                        help='Path of the dataset.',
                        required=True)
    parser.add_argument('-o',
                        '--origin',
                        dest='origin',
                        metavar='origin',
                        type=str,
                        help='Name of the origin city.',
                        required=True)
    parser.add_argument('-d',
                        '--destination',
                        dest='destination',
                        metavar='destination',
                        type=str,
                        help='Name of the destination city.',
                        required=True)
    parser.add_argument('-a',
                        '--algorithm',
                        dest='algorithm',
                        metavar='algorithm',
                        choices=['a*', 'csp', 'dijkstra'],
                        help="Name of the algorithm. Choices: ['a*', 'csp', 'dijkstra'].",
                        required=True)
    parser.add_argument('-hf',
                        '--heuristic',
                        dest='heuristic_function_name',
                        metavar='heuristic_function_name',
                        choices=['distance', 'duration', 'duration_distance', 'weighted'],
                        help="Name of the heuristic function. Choices: ['distance', 'duration', 'duration_distance', 'weighted'].",
                        required=True)

    parser.add_argument('-p',
                        '--print-graph',
                        action='store_true',
                        dest='print_graph',
                        help='[OPTIONAL] Enable generation of graph in GV and PNG format.')
    return parser


def get_heuristic_function(heuristic_function_name: str) -> Callable[[City, Connection, [City]], float | int]:
    if heuristic_function_name == 'distance':
        return hf_distance
    elif heuristic_function_name == 'duration':
        return hf_duration
    elif heuristic_function_name == 'duration_distance':
        return hf_duration_distance
    elif heuristic_function_name == 'weighted':
        return hf_weighted_duration_distance


def main():
    parser = parse_arguments()

    args = parser.parse_args()

    cities = parse_json_dataset(args.dataset_path)
    heuristic_function = get_heuristic_function(args.heuristic_function_name)

    if args.print_graph:
        print_graph(cities)

    check_data_validity(cities, args.origin, args.destination)
    compute(cities, args.algorithm, args.origin, args.destination, heuristic_function)


if __name__ == "__main__":
    main()
