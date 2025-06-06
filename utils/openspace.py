from table import Table


class OpenSpace:
    """
    This is a classroom...
    """
    def __init__(self, number_of_tables, seats_per_table):
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        # randomly assign people to Seat objects in the different Table objects
        pass

    def display(self):
        # display the different tables and there occupants
        # in a nice and readable way
        table_number = 1
        for table in self.tables:
            print(f"=== TABLE {table_number} ===")
            seat_numer = 1
            for seat in table.seats:
                print(f"Seat: {seat_numer} Occupant:{seat.occupant}")
                seat_numer += 1        
            table_number += 1

    def store(self, filename):
        # TODO: store the repartition in an excel file
        pass