class Cell:
    def __init__(self, distance, is_walkable, coordinates, room_text=None):
        self.distance = distance
        self.is_walkable = is_walkable
        self.coordinates = coordinates
        self.room_text = room_text

    def __repr__(self) -> str:
        return "Cell coords(x:" + str(self.coordinates[0]) + " y:" + str(self.coordinates[1]) + ")"
