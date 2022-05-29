import sys

from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset
from utils.graph_printer import print_graph


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
                f"ERROR. Invalid last parameter: expected '--print-tree' or nothing, but got '{args[4]}' instead.")

    check_data_validity(cities, args[1], args[2])

    if args[3] == 'A*':
        print('None')
        # compute_a(cities, args[3], args[1], args[2])
    elif args[3] == 'CSP':
        print('None')
        # compute_csp(cities, args[3], args[1], args[2])
    else:
        raise Exception(f"ERROR. Invalid algorithm parameter: Must be 'A*' or 'CSP', but got " + args[3] + " instead.")


if __name__ == "__main__":
    main()
