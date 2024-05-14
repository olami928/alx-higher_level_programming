#!/usr/bin/python3
"""
    this program divides the content of a matrix
"""
def matrix_divided(matrix, div):
    """divides all element of a list
        Args:
            matrix (list): the matrix list
            div(int, float): the divisor
        Returns:
            a new matrix that has been devided
        Raises:
            TypeError: if matrix is not a list of floats or int
            ZeroDivisionError: if div is 0
    """
    if div is None or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
             raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row = []

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(row)
    return new_matrix
