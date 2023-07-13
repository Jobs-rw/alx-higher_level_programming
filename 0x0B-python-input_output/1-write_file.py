def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written
    Args:
        filename (str): The name of the file
        text (str): The text to be written to the file
    Returns:
        int: The number of characters written to the file
    """
    if not isinstance(filename, str) or not isinstance(text, str):
        return 0

    count = 0
    with open(filename, 'w', encoding='utf-8') as file:
        count = file.write(text)

    return count
