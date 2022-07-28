#!/usr/bin/env python3
""" slice a matrix like a ninja """
import numpy as np


def np_slice(matrix, axes={}):
    """ slice a matrix """
    for key, val in axes.items():
        print('key: {}, val: {}'.format(key, val))
        if key == 1:
            return matrix[:, val[0]:val[1]]
        elif key == 2:
            return matrix[:, :, val[0]:val[1]:val[2]]
