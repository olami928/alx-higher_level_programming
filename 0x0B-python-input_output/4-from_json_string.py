#!/usr/bin/python3
"""This code an object (Python data structure) represented by a JSON string."""


import json


def from_json_string(my_str):
    """returns the json data structures ."""
    char = json.loads(my_str)
    return (char)
