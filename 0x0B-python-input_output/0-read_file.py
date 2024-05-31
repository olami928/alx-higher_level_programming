#!/usr/bin/python3
"""This code reada a text file and prints it to stdout"""

def read_file(filename=""):

    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end="")
