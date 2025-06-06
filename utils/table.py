class Seat:
    """
    Class to represent a seat
    """

    def __str__(self) -> str:
        return f"Free: {self.free} Occupant:{self.occupant}"

    def __init__(self, occupant: str = ""):
        self.occupant = occupant

    @property
    def free(self):
        return self.occupant == ""

    def set_occupant(self, occupant):
        self.occupant = occupant

    def remove_occupant(self):
        self.occupant = ""


class Table:
    """
    Class to represent a table
    """

    def __init__(self, capacity):
        self.seats = [Seat("") for _ in range(capacity)]

    def __str__(self) -> str:
        return f"Table has {self.left_capacity()} free seats"

    def has_free_spot(self) -> bool:
        return self.left_capacity() > 0
        
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self) -> int:
        free_seats = 0
        for seat in self.seats:
            if seat.free:
                free_seats += 1
        return free_seats
