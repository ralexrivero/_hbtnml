#!/usr/bin/env python3
""" add matrices """


def add_matrices(mat1, mat2):
    """ add two matrices """
    if len(mat1) != len(mat2):
        return None
    else:
        return mat1 + mat2
