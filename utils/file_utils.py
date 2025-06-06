# Create function to read input file

def read_colleagues_from_file(file_path):
    """
    This funtions reads colleague names from file...
    param file_path
    return list of names
    """
    colleagues = []

    # Open the file
    with open(file_path, "r") as file:
        # Read all colleagues in to the variable colleagues
        line = file.readline()
        while line:
            colleagues.append(line.rstrip())
            line = file.readline()

    # Return list of colleagues
    return colleagues
