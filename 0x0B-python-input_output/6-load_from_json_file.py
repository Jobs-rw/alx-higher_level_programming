import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    Args:
        my_obj (object): The object to be serialized and saved to the file
        filename (str): The name of the file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
