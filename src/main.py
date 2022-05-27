import sys

from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset
from utils.graph_generator import compute_graph
from utils.graph_printer import print_graph


def main():
    args: [] = sys.argv[1:]
    num_args: int = len(args)

    if num_args < 3:
        raise Exception(f'ERROR. Invalid number of arguments: expected at least 3 but got {num_args} instead.')

    cities, connections = parse_json_dataset(args[0])

    if num_args == 4:
        if args[3] == '--print-graph':
            print_graph(connections)
        else:
            raise Exception(
                f"ERROR. Invalid last parameter: expected '--print-tree' or nothing, but got '{args[1]}' instead.")

    cities = compute_graph(cities, connections)
    check_data_validity(cities, args[1], args[2])


if __name__ == "__main__":
    main()
