import json

from model.city import City
from model.connection import Connection


def parse_json_dataset(file_path: str) -> ([City], [Connection]):
    print(f"Reading file in '{file_path}'...")
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            info_dict = json.load(file)

            # Converting the cities to class
            cities: [City] = [City(**city) for city in info_dict['cities']]

            # Converting the connections to class
            # With the connections we need to do a little hack because of the 'from' reserved word
            for connection in info_dict['connections']:
                index_from = index_to = -1
                for index, item in enumerate(cities):
                    if item.name == connection['from']:
                        index_from = index
                    if item.name == connection['to']:
                        index_to = index
                cities[index_from].append_connection(
                    Connection(index_to, connection['distance'], connection['duration']))

            print("The dataset was parsed successfully.")
            return cities
    except EnvironmentError:
        raise Exception(f"ERROR. No file found in '{file_path}'.")
