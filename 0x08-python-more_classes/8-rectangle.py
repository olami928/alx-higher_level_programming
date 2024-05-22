#!/usr/bin/python3
"""This program defines a class of Rectangle."""


class Rectangle:
    """A class Rectangle that defines a rectangle.


    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """REturns the araea of the rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2*(self.__height + self.__width))

    def __str__(self):
        """REturns the string representation of the rectngle wih char '#'.


            if width or height equals 0, it returns an empty string.
        """

        rows = []

        if self.height == 0 or self.width == 0:
            return ""
        else:
            for i in range(self.height):
                rows.append(str(self.print_symbol) * self.width)
            return ('\n'.join(rows))

    def __repr__(self):
        """Returns thr string representation of thre class

        using eval() func.
        """

        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Deletes the insrance of rectangle and prints a messgae"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """checks if the two rectangle are equal, returns

            rect_1 if both are equal.


            Args:
                rect_1: the first rectangle
                rect_2: the second rectangle


            Raises:
                TypeError: if they are not instances of Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return (rect_1)
            else:
                return (rect_2)
