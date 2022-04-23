#!/usr/bin/env python3
""" matrix multiplication """


def mat_mul(mat1, mat2):
    """ matrix multiplication """
    if len(mat1[0]) != len(mat2):
        return None
    res = []

    for row1 in range(len(mat1)):
        for col2 in range(len(mat2[0])):
            for row2 in range(len(mat2)):
                print(mat1[][], mat2[][])
    return res
