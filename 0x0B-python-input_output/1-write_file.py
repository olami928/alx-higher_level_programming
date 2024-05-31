#!/usr/bin/python3
"""This code writes to a textfile"""


def write_file(filename="", text=""):
    """This code writes to a file, creates it if it does not exists"""

    with open(filename, 'w', encoding='UTF-8') as f:
        no_char = f.write(text)
        return (no_char)
