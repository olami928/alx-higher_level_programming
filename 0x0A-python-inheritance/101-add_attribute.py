#!/usr/bin/python3
"""This program adds an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
