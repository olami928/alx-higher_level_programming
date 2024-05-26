#!/usr/bin/python3
"""This defines a class BaseGeometry"""


class BaseGeometry:
    """This is the class defintion"""
    pass

    def area(self):
        """This is an istance of BaseGeometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This instance validates an int.

            Args:
                name (int): the int string to hold the int
                value (int): the string int

            Raises:
                TypeError: if value is not an int.

            ValueError:
                ValueError: if value is <= 0


        """
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.name = value


class Rectangle(BaseGeometry):
    """This a class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """This is the instantation of width and height

            Args:
                width (int): the width of the rectangle
                height (int): the height of  the rectangle
        """

        self.__width = width
        self.__height = height
