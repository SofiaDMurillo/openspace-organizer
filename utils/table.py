class Seat:
    """
    This is a seat...
    """

    def __init__(self, occupant):
        self.occupant = occupant
        self.free = occupant == ""

    def set_occupant(self, occupant):
        self.occupant = occupant
        self.free = False

    def remove_occupant(self):
        self.occupant = ""
        self.free = True

    def __str__(self) -> str:
        return f"Free: {self.free} Occupant:{self.occupant}"


class Table:
    """
    This is a table...
    """

    def __init__(self, capacity):
        self.seats = [Seat("") for _ in range(capacity)]

    def __str__(self) -> str:
        return f"Table has {len(self.seats)} seats"
