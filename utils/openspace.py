import random
from utils.table import Table


class OpenSpace:
    """
    Class to represent a classroom
    """
    def __init__(self, number_of_tables, seats_per_table):
        self.tables = [Table(seats_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        # Randomize the names in the list
        random.shuffle(names)

        table_num = 0
        while len(names):
            # Get current table
            current_table = self.tables[table_num]
            
            # Take a name from the list
            current_name = names.pop()

            current_table.assign_seat(current_name)
            
            # Change to the next table
            table_num += 1
            # If we reach the last table, change to the first table
            if table_num == len(self.tables):
                table_num = 0          

    def display(self):
        # Display the different tables and there occupants
        # in a nice and readable way
        table_number = 1

        for table in self.tables:

            print(f"=== TABLE {table_number} ===")

            seat_numer = 1

            for seat in table.seats:
                print(f"Seat {seat_numer}: {seat.occupant}")
                seat_numer += 1    

            table_number += 1