class Cell:
    def __init__(self, distance, is_walkable, coordinates, weight):
        self.distance = distance
        self.is_walkable = is_walkable
        self.coordinates = coordinates
        self.weight = weight

    def __repr__(self) -> str:
        return str(self.is_walkable) + " Cell coords(x:" + str(self.coordinates[0]) + " y:" + str(self.coordinates[1]) + ")"
