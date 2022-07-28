#!/usr/bin/env python3
""" slice a matrix like a ninja """
import numpy as np


def np_slice(matrix, axes={}):
    """ slice a matrix """
    for key, val in axes.items():
        start = val[0]
        end = val[1]
        return matrix.take(range(start, end), key)
