from queue import PriorityQueue
from typing import Callable

from model.city import City
from model.connection import Connection


def compute_dijkstra(cities: [City],
                     from_city_name: str,
                     value_getter: Callable[[Connection, [City]], float | int]) -> dict[str, float]:
    visited: [str] = []

    search_space = {city.name: float('inf') for city in cities}
    search_space[from_city_name] = 0

    from_city: City = get_city_by_name(cities, from_city_name)
    pq = PriorityQueue()
    pq.put((0, from_city))

    while not pq.empty():
        current_distance, current_city = pq.get()
        visited.append(current_city.name)

        for connection in current_city.connections:
            neighbor: City = cities[connection.to_id]

            if neighbor.name not in visited:
                new_cost: float = search_space[current_city.name] + value_getter(connection)
                if new_cost < search_space[neighbor.name]:
                    pq.put((new_cost, neighbor))
                    search_space[neighbor.name] = new_cost

    return search_space


def get_city_by_name(cities: [City], city_name: str) -> City | None:
    for city in cities:
        if city.name == city_name:
            return city

    return None
