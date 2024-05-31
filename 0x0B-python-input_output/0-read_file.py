#!/usr/bin/python3
"""This code reada a text file and prints it to stdout"""


def read_file(filename=""):
    """This is the code that read a text file and prints it to stdout"""

    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end="")
