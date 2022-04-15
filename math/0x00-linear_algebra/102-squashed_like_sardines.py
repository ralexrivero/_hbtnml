#!/usr/bin/env python3
""" concatenate two matrices along a specific axis """
import numpy as np


def cat_matrices(mat1, mat2, axis=0):
    """ concatenate two matrices along a specific axis """
    if len(mat1) != len(mat2):
        return None
    else:
        return np.concatenate((mat1, mat2), axis=axis)
