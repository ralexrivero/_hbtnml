#!/usr/bin/env python3
""" slice a matrix like a ninja """


def np_slice(matrix, axes={}):
    """ slice a matrix """
    return matrix[tuple(axes.get(i, slice(None)) for i in range(matrix.ndim))]
