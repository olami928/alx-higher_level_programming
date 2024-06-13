#!/usr/bin/python3
"""
This code  returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """This code returns the dictionary representation of a data."""

    return (vars(obj))
