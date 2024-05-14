#!/usr/bin/python3
"""
    this function prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """

        Args:
            first_name (string): the first name
            last_name (string): the last name.

        Returns:
            the full name.

        Raises:
            TypeError: if first_name of last_name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
