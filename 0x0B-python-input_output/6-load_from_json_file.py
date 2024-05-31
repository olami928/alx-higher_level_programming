#!/usr/bin/python3
"""This code  creates an Object from a “JSON file”."""


import json


def load_from_json_file(filename):
    """This code creates an object."""
    with open(filename, 'r', encoding='UTF-8') as f:
        json.load(f)
