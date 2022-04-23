#!/usr/bin/env python3
""" matrix multiplication """


def mat_mul(mat1, mat2):
    """ matrix multiplication """
    if len(mat1[0]) != len(mat2):
        return None

    res = []

    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(0)
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]

    return res
