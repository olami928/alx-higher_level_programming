#!/usr/bin/python3
"""
    This program checks if the object is

    an instance of the specifed class.

"""


def is_same_class(obj, a_class):

    """This code checks for the instance"""

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
