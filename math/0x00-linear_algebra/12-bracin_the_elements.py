#!/usr/bin/env python3
""" addition, subtraction, multiplication and division of matrices """


def np_elementwise(mat1, mat2):
    """
    elementwise addition, subtraction,
    multiplication and division of matrices
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
