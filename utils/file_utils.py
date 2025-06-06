def read_colleagues_from_file(file_path):
    """
    This funtions reads colleague names from a file.

    Parameters:
        file_path (str): The path to the file containing the list of names

    Returns:
        The names in a list of strings
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
