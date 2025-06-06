from utils.file_utils import read_colleagues_from_file
from utils.openspace import OpenSpace

# Load the colleagues from the excel file defined in the config file
colleagues = read_colleagues_from_file("./inputs/colleagues.csv")
print(colleagues)

# Launch the organizer
open_space = OpenSpace(6, 5)

# Distribute the colleagues
open_space.organize(colleagues)

# Display the results
open_space.display()