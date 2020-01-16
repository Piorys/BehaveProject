import json
import __root__ as root

def parse_data_object(filename):
    """
    Parses JSON data object

    :param filename: - filename of JSON data object without extension ie. Environments for Environments.json
    :return: - Accessible Data Object
    """

    with open(root.path()+'/src/data/'+filename+".json", 'r') as f:
        return json.load(f)

