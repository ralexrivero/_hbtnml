#!/usr/bin/env python3
""" slice a matrix like a ninja """
import numpy as np


def np_slice(matrix, axes={}):
    """ slice a matrix """
    sliced = []
    obj = [slice(None)] * (max(axes) + 1)
    for key, val in axes.items():
        obj[key] = slice(*val)
    sliced = matrix[tuple(obj)]
    return sliced