#!/usr/bin/env python3
""" concatenate two matrices along a specific axis """


def matrix_shape(matrix):
    """ Shape size of a matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """ concatenate two matrices along a specific axis """
    # size control
    s1 = matrix_shape(mat1)
    s2 = matrix_shape(mat2)
    if s1 != s2:
        return None
    else:
        return np.concatenate((mat1, mat2), axis=axis)
