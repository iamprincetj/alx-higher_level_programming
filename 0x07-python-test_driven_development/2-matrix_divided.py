#!/usr/bin/python3
""" module that divides all elements of a matrix of similar sized rows """


def matrix_divided(matrix, div):
    """ function that returns a new matrix with each element divided by da div

    Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error

    Returns: a new matrix with each element adjusted to the div amount
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_list = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(msg)
    if type(div) is int or type(div) is float or div is None:
        pass  # improper div value type checks
    else:
        raise TypeError("div must be a number")
    if div == 0:  # if div is zero
        raise ZeroDivisionError("division by zero")
    if matrix[0]:  # if matrix is empty or not
        len_mat = len(matrix[0])
    else:
        raise TypeError(msg)
    size_msg = "Each row of the matrix must have the same size"

    for i in range(len(matrix)):  # real work. the appending
        if len(matrix[i]) is not len_mat:
            raise TypeError(size_msg)
        new_list.append([])
        for j in matrix[i]:
            if type(j) is int or type(j) is float:
                new_list[i].append(round(j / div, 2))
            else:
                raise TypeError(msg)
    return new_list
