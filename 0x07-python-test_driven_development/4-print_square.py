#!/usr/bin/python3
# this program prints a square with #

def print_square(size):
    """ This program prints a square with # 
        
        Args:
            size (int): the size of the sqare.


        Raises:
            ValueError: if size <= 0
            TypeError: if size is not an int and less than 0


        Return:
            The square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
