from model.city import City


class AnnotatedCity:
    city: City
    path: [City]
    acc_weight: float

    def __init__(self, city: City, path: [City], acc_weight: float):
        self.city = city
        self.path = path
        self.acc_weight = acc_weight
