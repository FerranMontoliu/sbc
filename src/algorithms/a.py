from model.annotated_city import AnnotatedCity
from model.city import City
from model.connection import Connection


def compute_a(cities: [City], from_city_name: str, to_city_name: str, value_getter) -> ([City], float):
    node_list: [AnnotatedCity]
    path: [City] = []
    acc_weight: float = 0

    # Get the origin city
    from_city: City | None = None
    for city in cities:
        if city.name == from_city_name:
            from_city = city
            break

    current_city: City = from_city
    node_list = [AnnotatedCity(current_city, [], 0)]

    while node_list:
        # If the current node is the destination, finish
        if current_city.name == to_city_name:
            return path, acc_weight

        if current_city.connections:
            current_city, weight = get_min_path_node(current_city.connections, cities, value_getter)
            path.append(current_city)
            acc_weight += weight

    return path, acc_weight


def get_min_path_node(connections: [Connection], cities: [City], value_getter) -> (City, float):
    min_val: float = 0
    min_connection: Connection | None = None

    for connection in connections:
        connection_weight: float = value_getter(connection)
        if min_val == 0 or connection_weight < min_val:
            min_val = connection_weight
            min_connection = connection

    for city in cities:
        if city.name == min_connection.to_name:
            return city, min_val
