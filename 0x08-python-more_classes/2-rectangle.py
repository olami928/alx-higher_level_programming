#!/usr/bin/python3
""" This program defines a class of 
    Rectangle
"""

class Rectangle:
    """ A class Rectangle that defines a rectangle
    Attributes:
        width
    """
    @property
    def width(self):
        """ Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self):
        """ defines the width of a rectangle

        Args:
            width (int): the width of the rectangle

        Raises:
            TypeError: if not an int
            ValueError: if it is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self):
        """ defines the width of the rectangle

        Args:
            height (int): the height of the rectangle.
            
        Raises:
            TypeError: if it is not an int
            ValueError: if it is less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        # instantation with optional width and height
    def __init__(self, width = 0, height = 0):
        """ initializes the rectnagle with width and height
        Args:
            width (int): the width
            height (int): the height
        """
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the rectangle
        Args:
            area (int): the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle
        """
        return (2 *(self.__width + self.__height))

