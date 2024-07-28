#!/usr/bin/python3
"""This code finds a peak in the list of integers."""


def find_peak(list_of_integers):
    """
    Find a peak element in the list of integers.
    A peak element is greater than or equal to its neighbors.
    """
    max_n = None
    for ele in list_of_integers:
        if max_n is None or max_n < ele:
            max_n = ele
    return (max_n)
