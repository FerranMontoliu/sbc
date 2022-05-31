from model.city import City


class CSPNode:
    city: City

    def __init__(self, city: City):
        self.city = city
