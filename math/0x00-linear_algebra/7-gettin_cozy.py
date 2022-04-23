#!/usr/bin/env python3
""" concatenates two matrices """


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices """
    if (axis != 0 and axis != 1):
        return None
    elif (len(mat1) != len(mat2)):
        return None
    elif axis == 0:
        matCon = []
        for row in mat1:
            matCon.append(row.copy())
        for row in mat2:
            matCon.append(row.copy())
    else:
        matCon = []
        for i in range(len(mat1)):
            matCon.append([])
            matCon[i] = mat1[i] + mat2[i]
    return matCon
