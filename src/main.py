import sys

from utils.file_reader import parse_json_dataset


def main():
    args: [] = sys.argv[1:]
    num_args: int = len(args)

    if num_args != 1:
        raise Exception(f'ERROR. Invalid number of arguments: expected 1 but got {num_args} instead.')

    cities, connections = parse_json_dataset(args[0])


if __name__ == "__main__":
    main()
