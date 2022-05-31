class Connection:
    to_id: int
    distance: int
    duration: int

    def __init__(self, to_id: int, distance: int, duration: int):
        self.to_id = to_id
        self.distance = distance
        self.duration = duration
