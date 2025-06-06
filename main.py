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

sample_table = Table(5)
print(sample_table)

sample_table.seats[0].set_occupant("Sofia")
sample_table.seats[1].set_occupant("Alberto")

for seat in sample_table.seats:
    print(seat)



