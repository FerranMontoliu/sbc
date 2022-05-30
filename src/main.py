from argparse import ArgumentParser
from typing import Callable, Literal

from algorithms.a import compute_a
from algorithms.csp import compute_csp
from model.city import City
from model.connection import Connection
from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset
from utils.graph_printer import print_graph


def compute(cities: [City],
            algorithm: Literal['a*', 'csp'],
            from_city: str,
            to_city: str,
            heuristic_function: Callable[[Connection], float | int]) -> ([City], float):
    print('Computing algorithm...')
    if algorithm == 'a*':
        path, acc_weight = compute_a(cities, from_city, to_city, heuristic_function)
    elif algorithm == 'csp':
        path, acc_weight = compute_csp(cities, from_city, to_city, heuristic_function)
    else:
        raise Exception(f"ERROR. Invalid algorithm parameter: Must be 'a*' or 'csp', but got '{algorithm}' instead.")
    print('Search finished.')

    print(f"The best route found is: {[c.name for c in path]}.")
    print(f"With a cost of {acc_weight}.")


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
                        choices=['a*', 'csp'],
                        help="Name of the algorithm. Choices: ['a*', 'csp'].",
                        required=True)

    parser.add_argument('-p',
                        '--print-graph',
                        action='store_true',
                        dest='print_graph',
                        help='[OPTIONAL] Enable generation of graph in GV and PNG format.')
    return parser


def main():
    def hf_distance(c: Connection) -> int:
        return c.distance

    def hf_duration(c: Connection) -> int:
        return c.duration

    def hf_duration_distance(c: Connection) -> int:
        return c.duration * c.distance

    parser = parse_arguments()

    args = parser.parse_args()

    cities = parse_json_dataset(args.dataset_path)

    if args.print_graph:
        print_graph(cities)

    check_data_validity(cities, args.origin, args.destination)
    compute(cities, args.algorithm, args.origin, args.destination, hf_distance)


if __name__ == "__main__":
    main()
