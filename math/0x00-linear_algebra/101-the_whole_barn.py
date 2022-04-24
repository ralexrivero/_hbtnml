#!/usr/bin/env python3
""" add matrices """

def matrix_shape(matrix):
    """ Shape size of a matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def add_matrices(mat1, mat2):
    """ add two matrices """
    # size control
    s1 = matrix_shape(mat1)
    s2 = matrix_shape(mat2)
    if s1 != s2:
        return None

    add = []

    return add

