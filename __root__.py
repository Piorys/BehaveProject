import os


def path():
    """
    Returns path to root file, which gives us root directory of project
    :return: path to root folder of project
    """
    return os.path.dirname('__root__.py')
