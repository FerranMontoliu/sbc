import sys
import numpy

from model.city import City
from model.csp_node import CSPNode


# Variable: cities, Value: connections
def compute_csp(cities: [City], from_city: str, to_city: str, value_getter) -> ([City], float):
    node_matrix: [[CSPNode]] = prepare_nodelist(cities, value_getter)
    index_path, cost = backtracking_search(node_matrix, [] + [get_city(cities, from_city)], get_city(cities, to_city), 0)
    cities_path = []
    for index in index_path:
        cities_path.append(cities[index])
    return cities_path, cost


def backtracking_search(node_matrix: [[CSPNode]],
                        path: [int],
                        to_city: int,
                        acc_weight: float) -> ([City], float):
    # End condition
    if path[-1] == to_city:
        return path, acc_weight

    node_matrix_aux = node_matrix.copy()
    path_aux = path.copy()

    while exist_children(node_matrix_aux, path):
        variable_column = path_aux[-1]
        value_row = get_less_restrictive_value(node_matrix, variable_column)
        path_aux.append(value_row)
        acc_weight += node_matrix_aux[variable_column, value_row]
        node_matrix_aux = apply_restrictions(node_matrix_aux, path_aux)
        return backtracking_search(node_matrix_aux, path_aux, to_city, acc_weight)
    return None, None


def exist_children(node_matrix: [[CSPNode]], path: [int]) -> bool:
    for to_index in range(len(node_matrix)):
        if node_matrix[path[-1], to_index] != -1:
            return True
    return False


def apply_restrictions(node_matrix: [[CSPNode]], path: [int]) -> [[CSPNode]]:
    for i in range(len(node_matrix[0])):
        node_matrix[i, path[-2]] = -1
        node_matrix[path[-2], i] = -1
        node_matrix[i, path[-1]] = -1
    return node_matrix


def prepare_nodelist(cities: [City], value_getter) -> [[CSPNode]]:
    matrix: [CSPNode] = numpy.empty(shape=(len(cities), len(cities)))
    for i in range(len(cities)):
        for j in range(len(cities)):
            matrix[i, j] = -1
        for connection in cities[i].connections:
            matrix[i, connection.to_id] = value_getter(cities[connection.to_id], connection, [] + [cities[i]])
    return matrix


def get_most_restrictive_variable(node_matrix: [[CSPNode]]) -> int:
    max_connections = 0
    max_connections_city = -1
    for i in range(len(node_matrix)):
        connections = 0
        for j in range(len(node_matrix)):
            if node_matrix[i, j] != -1:
                connections += 1
        if connections > max_connections:
            max_connections = connections
            max_connections_city = i
    return max_connections_city


def get_less_restrictive_value(node_matrix: [[CSPNode]], node: int) -> int:
    less_total_connections = sys.maxsize
    less_connections_index = -1
    possible_values = []
    for i in range(len(node_matrix)):
        if node_matrix[node, i] != -1:
            possible_values.append(i)

    for i in possible_values:
        connections = 0
        for j in range(len(node_matrix)):
            if node_matrix[j, i] != -1:
                connections += 1
        if less_total_connections > connections > 0:
            less_total_connections = connections
            less_connections_index = i

    return less_connections_index


def get_city(cities: [City], city_name: str) -> int:
    for i in range(len(cities)):
        if city_name == cities[i].name:
            return i
    return -1
