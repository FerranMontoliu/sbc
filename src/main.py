import sys

from utils.file_reader import parse_json_dataset
from utils.graph_generator import compute_graph
from utils.graph_printer import print_graph


def main():
    args: [] = sys.argv[1:]
    num_args: int = len(args)

    if num_args < 1:
        raise Exception(f'ERROR. Invalid number of arguments: expected 1 but got {num_args} instead.')

    cities, connections = parse_json_dataset(args[0])

    if num_args == 2:
        if args[1] == '--print-graph':
            print_graph(connections)
        else:
            raise Exception(f"ERROR. Invalid second parameter: expected '--print-tree' but got '{args[1]}' instead.")

    cities = compute_graph(cities, connections)


if __name__ == "__main__":
    main()
