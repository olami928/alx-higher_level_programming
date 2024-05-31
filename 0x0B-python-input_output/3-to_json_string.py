#!/usr/bin/python3
"""This code returns the JSON representation of an object (string)."""


import json


def to_json_string(my_obj):
    """returns the jSON repr of a string."""
    char = json.dumps(my_obj)
    return (char)
