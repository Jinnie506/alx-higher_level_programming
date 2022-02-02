#!/usr/bin/python3
"""
Contains the "pascal_triangle" function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    matrix = []
    if n <= 0:
        return(matrix)

    for i in range(n):
        matrix.append([])
        matrix[i].append(1)
        for j in range(1, i):
            matrix[i].append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        if (i != 0):
            matrix[i].append(1)
    return(matrix)
