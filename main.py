# Openspace organizer project
# Import everything you need to launch the organizer

from utils.file_utils import read_colleagues_from_file
from utils.table import Seat

# Import openspace and import tables

# Load the colleagues from the excel file defined in the config file

# Launch the organizer

# Display the results

#print(read_colleagues_from_file("inputs/colleagues.csv"))

seat1 = Seat("Sofia")
print(f"Is it free: {seat1.free}")
print(f"who is in the seat: {seat1.occupant}")
seat1.remove_occupant()
print(f"Is it free: {seat1.free}")
print(f"who is in the seat: {seat1.occupant}")

