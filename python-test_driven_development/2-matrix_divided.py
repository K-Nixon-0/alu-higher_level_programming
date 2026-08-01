#!/usr/bin/python3
"""Module for dividing all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals"""
    if (type(matrix) is not list or len(matrix) == 0 or
            not all(type(row) is list for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(type(n) in (int, float) for n in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
