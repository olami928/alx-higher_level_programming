#!/usr/bin/python3
"""This is a class defintion of a rectangle."""


from models.base import Base


class Rectangle(Base):
    """This is a class definition of Recatngle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the initialization of the Recatngle class."""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""

        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle."""

        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x value of the rectangle."""

        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the x value of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y value of the rectangle."""

        return (self.__x)

    @y.setter
    def y(self. value):
        """sets the value of y of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the value of the Rectangle instance."""

        return (self.__width * self.__height)

    def display(self):
        """this code prints the rectangle instance with the character '#'."""

        rows = []

        if self.__width or self.__height == 0:
            return ""
        else:
            for i in range(self.height):
                rows.append("#" * self.width)
            return ('\n'.join(rows))

    def __str__(self):
        """This is a string representation of rectangle."""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
