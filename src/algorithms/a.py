from model.annotated_city import AnnotatedCity
from model.city import City


def compute_a(cities: [City], from_city_name: str, to_city_name: str, value_getter) -> ([City], float):
    node_list: [AnnotatedCity]
    acc_weight: float = 0

    # Get the origin city
    from_city: City | None = None
    for city in cities:
        if city.name == from_city_name:
            from_city = city
            break
    node_list = [AnnotatedCity(from_city, [], 0)]

    while node_list:
        # Check if the city was not already visited. Discard otherwise
        while len(node_list) > 0:
            node = node_list.pop(0)
            if not is_visited(node.path, node.city):
                break
        acc_weight = node.acc_weight

        # If the current node is the destination, finish
        if node.city.name == to_city_name:
            return list_append(node.path, node.city), acc_weight

        # Save all its connections for further checks
        for connection in node.city.connections:
            path_aux = node.path.copy()
            node_list.append(
                AnnotatedCity(cities[connection.to], list_append(path_aux, node.city),
                              acc_weight + value_getter(connection)))

        # Sort list on every iteration to have an ordered list
        node_list.sort(key=lambda x: x.acc_weight)
    return None, None


# Check if the item is in the list or not
def is_visited(lst, item) -> bool:
    for city in lst:
        if city == item:
            return True
    return False


# Append element on the list and return the result
def list_append(lst, item):
    lst.append(item)
    return lst
