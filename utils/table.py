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
