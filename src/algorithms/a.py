from typing import Callable

from model.annotated_city import AnnotatedCity
from model.city import City
from model.connection import Connection


def compute_a(cities: [City],
              from_city_name: str,
              to_city_name: str,
              value_getter: Callable[[Connection, [City]], float | int]) -> ([City], float):
    # Get the origin city
    from_city: City | None = None
    for city in cities:
        if city.name == from_city_name:
            from_city = city
            break

    node_list: [AnnotatedCity] = [AnnotatedCity(from_city, [], 0)]
    acc_weight: float = 0

    while node_list:
        # Check if the city was not already visited. Discard otherwise
        node = node_list.pop(0)
        if node:
            acc_weight = node.acc_weight

        # If the current node is the destination, finish
        if node.city.name == to_city_name:
            return node.path + [node.city], acc_weight

        # Save all its connections for further checks
        for connection in node.city.connections:
            node_list.append(
                AnnotatedCity(cities[connection.to_id], node.path + [node.city],
                              acc_weight + value_getter(connection, node.path)))

        # Sort list on every iteration to_id have an ordered list
        node_list.sort(key=lambda x: x.acc_weight)
        # Delete duplicates that are less optimal
        node_list = list(filter(lambda n: not duplicate(n, node_list), node_list))
    return None, None


# Check for duplicates previous as the one found
def duplicate(node: AnnotatedCity, node_list: [AnnotatedCity]) -> bool:
    index = node_list.index(node)
    for i in range(index):
        if node_list[i].city.name == node.city.name:
            return True
    return False


# Check if the item is in the list or not
def is_visited(cities_list: [City], current_city: City) -> bool:
    for city in cities_list:
        if city == current_city:
            return True
    return False
