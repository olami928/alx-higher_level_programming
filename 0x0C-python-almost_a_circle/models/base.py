#!/usr/bin/python3
"""This is a class definition of Base."""


class Base:
    """This is the defintion of the Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the initialization of the Base class."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
