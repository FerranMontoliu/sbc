class Connection:
    from_name: str
    to_name: str
    distance: str
    duration: str

    def __init__(self, from_: str, to: str, distance: str, duration: str):
        self.from_name = from_
        self.to_name = to
        self.distance = distance
        self.duration = duration
