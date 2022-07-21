""" Tries to find a file in any OS. """

from os import path


def find(file: str) -> str:
    """ Returns the absolute path to a file. File should be at least a relative path
    which will be searched. """
    return path.abspath(file)
