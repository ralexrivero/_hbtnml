#!/usr/bin/env python3
""" concatenate two matrices along a specific axis """


def matrix_shape(matrix):
    """
        Shape size of a matrix
        All elements in the same dimension are of the same type/shape
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """ concatenate two matrices along a specific axis """
    cated = []

    if type(mat1) is not type(mat2) or type(mat1) is not list:
        return None
    if axis == 0:
        s1 = matrix_shape(mat1)
        s2 = matrix_shape(mat2)
        if len(s1) != len(s2) or (len(s1) > 0 and s1[1:] != s2[1:]):
            return None
        cated = mat1 + mat2
    else:
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat1)):
            row = cat_matrices(mat1[i], mat2[i], axis=(axis - 1))
            if row is None:
                return None
            cated.append(row)
    return cated
