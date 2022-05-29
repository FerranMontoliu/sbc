import sys

from algorithms.a import compute_a
from algorithms.csp import compute_csp
from model.city import City
from model.connection import Connection
from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset
from utils.graph_printer import print_graph


def compute(cities: [City], algorithm: str, from_city: str, to_city: str) -> ([City], float):
    def hf_distance(c: Connection) -> int:
        return c.distance

    def hf_duration(c: Connection) -> int:
        return c.duration

    def hf_duration_distance(c: Connection) -> int:
        return c.duration * c.distance

    if algorithm == 'A*':
        path, acc_weight = compute_a(cities, from_city, to_city, hf_duration)
    elif algorithm == 'CSP':
        path, acc_weight = compute_csp(cities, from_city, to_city, hf_duration)
    else:
        raise Exception(f"ERROR. Invalid algorithm parameter: Must be 'A*' or 'CSP', but got {algorithm} instead.")
    print(f"The best route found is:")
    print([c.name for c in path])
    print(f"With a cost of {acc_weight}")


def main():
    args: [] = sys.argv[1:]
    num_args: int = len(args)

    if num_args < 4:
        raise Exception(f'ERROR. Invalid number of arguments: expected at least 4 but got {num_args} instead.')

    cities = parse_json_dataset(args[0])

    if num_args == 5:
        if args[4] == '--print-graph':
            print_graph(cities)
        else:
            raise Exception(
                f"ERROR. Invalid last parameter: expected '--print-tree' or nothing, but got {args[4]} instead.")

    check_data_validity(cities, args[1], args[2])
    compute(cities, args[3], args[1], args[2])


if __name__ == "__main__":
    main()
