#!/usr/bin/python3
# this program eturns the list of available attributes and methods of an object
"""This program returns the list of avaulable methods of an object."""


def lookup(obj):
    """ This program list available attribue of an object

        Args:
            obj: the obj to be tested

        Returns:
            A list
    """
    return (dir(obj))
