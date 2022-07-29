#!/usr/bin/env python3
""" slice a matrix like a ninja """


def np_slice(matrix, axes={}):
    """ slice a matrix """
    obj = [slice(None)] * (max(axes) + 1)
    for key, val in axes.items():
        obj[key] = slice(*val)
    sliced = matrix[tuple(obj)].copy()
    return sliced
