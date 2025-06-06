from math import ceil
from utils.file_utils import read_colleagues_from_file
from utils.openspace import OpenSpace

# Load the colleagues from the excel file defined in the config file
colleagues = read_colleagues_from_file("./inputs/colleagues.csv")

# Launch the organizer
num_tables = 6
num_seats = ceil(len(colleagues) / num_tables)
open_space = OpenSpace(num_tables, num_seats)

# Distribute the colleagues
open_space.organize(colleagues)

# Display the results
open_space.display()
