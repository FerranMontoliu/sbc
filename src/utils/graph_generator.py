from model.city import City
from model.connection import Connection


def compute_graph(cities: [City], connections: [Connection]) -> [City]:
    print('Computing graph...')
    for connection in connections:
        for city in cities:
            if connection.from_name == city.name:
                city.connections.append(connection)

    print('Graph computed successfully.')
    return cities
