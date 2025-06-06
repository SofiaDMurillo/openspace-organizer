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


class Table:
    """
    This is a table...
    """

    pass
