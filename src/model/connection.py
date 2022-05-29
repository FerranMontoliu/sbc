class Connection:
    to: int
    distance: int
    duration: int

    def __init__(self, to: int, distance: int, duration: int):
        self.to = to
        self.distance = distance
        self.duration = duration
