#!/usr/bin/python3
"""This code appends to a textfile"""


def append_write(filename="", text=""):
    """This code appends to a file, creates it if it does not exists"""

    with open(filename, 'a', encoding='UTF-8') as f:
        no_char = f.write(text)
        return (no_char)
