class City:
    name: str
    address: str
    country: str
    latitude: float
    longitude: float

    def __init__(self, name: str, address: str, country: str, latitude: float, longitude: float):
        self.name = name
        self.address = address
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
