#!/usr/bin/python3
"""This code  writes an Object to a text file, using a JSON representation:"""


import json


def save_to_json_file(my_obj, filename):
    """This code writes to a text file."""
    with open(filename, 'w', encoding='UTF-8') as f:
        no_char = json.dump(my_obj, f)
        return (no_char)
