#!/usr/bin/python3
"""This code shows a locked class."""


class LockedClass:
    """
    A class that allows only an instance attribute called 'first_name'.
    This class prevents the user from dynamically creating new instance
    attributes except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ['first_name']
