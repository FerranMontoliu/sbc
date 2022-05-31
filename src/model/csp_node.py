from model.connection import Connection


class CSPNode:
    cost_from: float

    def __init__(self, city):
        self.city = city
        self.possible_connections = []

