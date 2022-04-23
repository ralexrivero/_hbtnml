#!/usr/bin/env python3
""" concatenates two matrices """


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices """
    if type(mat1) is not list\
       or type(mat2) is not list\
       or not len(mat1)\
       or not len(mat2):
        return None
    if (axis != 0 and axis != 1):
        return None
    elif axis == 0:
        if (len(mat1[0]) != len(mat2[0])):
            return None
        matCon = []
        for row in mat1:
            matCon.append(row.copy())
        for row in mat2:
            matCon.append(row.copy())
    else:
        if (len(mat1) != len(mat2)):
            return None
        matCon = []
        for i in range(len(mat1)):
            matCon.append([])
            matCon[i] = mat1[i] + mat2[i]
    if type(matCon[0]) is not list or type(matCon) is not list:
        return None
    return matCon
