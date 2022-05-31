from model.city import City
from model.connection import Connection


def hf_distance(destination_city: City, c: Connection, path: [City] = None) -> float:
    if path and destination_city.name == path[-1].name:
        return float('inf')
    return c.distance


def hf_duration(destination_city: City, c: Connection, path: [City] = None) -> float:
    if path and destination_city.name == path[-1].name:
        return float('inf')
    return c.duration


def hf_duration_distance(destination_city: City, c: Connection, path: [City] = None) -> float:
    if path and destination_city.name == path[-1].name:
        return float('inf')
    return c.duration * c.distance


def hf_weighted_duration_distance(destination_city: City, c: Connection, path: [City] = None) -> float:
    if path and destination_city.name == path[-1].name:
        return float('inf')
    return 0.7 * c.duration + 0.3 * c.distance
