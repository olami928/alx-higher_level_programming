#!/usr/bin/python3
# this program adds two integer together
def add_integer(a, b=98):
    """ This code adds two integer.

    Args:
        a: the first integer.
        b: the second integer.
    
    Return:
        int sum of 'a' and 'b' 
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not  isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
