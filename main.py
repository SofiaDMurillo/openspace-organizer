# Openspace organizer project
# Import file utils
from utils.file_utils import read_colleagues_from_file
# Import openspace, tables and seats
from utils.table import Seat
from utils.table import Table


# Load the colleagues from the excel file defined in the config file

# Launch the organizer

# Display the results

#print(read_colleagues_from_file("inputs/colleagues.csv"))

sample_table = Table(4)
print(sample_table)

sample_table.assign_seat("Sofia")
sample_table.assign_seat("Alberto")

print(f"left capacity={sample_table.left_capacity()}")
print(f"has free spot={sample_table.has_free_spot()}")

for seat in sample_table.seats:
    print(seat)



