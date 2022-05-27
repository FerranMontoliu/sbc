import json

from model.city import City
from model.connection import Connection


def parse_json_dataset(file_path: str) -> ([City], [Connection]):
    print(f"Reading file in '{file_path}'...")
    try:
        with open(file_path, "r") as file:
            info_dict = json.load(file)

            # Converting the cities to class
            cities: [City] = [City(**city) for city in info_dict['cities']]

            # Converting the connections to class
            # With the connections we need to do a little hack because of the 'from' reserved word
            connections: [Connection] = []
            for connection in info_dict['connections']:
                connection['from_'] = connection.pop('from')
                connections.append(Connection(**connection))

            print("The dataset was parsed successfully.")
            return cities, connections
    except EnvironmentError:
        raise Exception(f"ERROR. No file found in '{file_path}'.")
