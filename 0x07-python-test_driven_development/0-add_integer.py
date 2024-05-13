#!/usr/bin/python3
# this program adds two integer together
def add_integer(a, b=98):
    """ This code adds two integer.

    Args:
        a (int): the first integer.
        b (int): the second integer.
    Return:
        int sum of 'a' and 'b'
    Raises:
        TypeError: if a or b is not an int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
