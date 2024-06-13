#!/usr/bin/python3
"""
This code insets a text to a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This code insets a text to a file after each line containing
    a specific string.


    args:
        search_string(string): the string to be searched
        new_string(string): the new string
    """

    lines = []

    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    with open(filename, 'w', encoding='UTF-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
