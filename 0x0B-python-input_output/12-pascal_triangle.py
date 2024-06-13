#!/usr/bin/python3
"""This is returns a pascal triangle."""


def pascal_triangle(n):
    """
    This program returns a list of integers representation the
    pascal triangle of n:

    args:
        n: the lenght
    """

    if n <= 0:
        return []

    tri = [[1]]

    for i in range(1, n):
        prev_row = tri[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        tri.append(new_row)
    return tri
