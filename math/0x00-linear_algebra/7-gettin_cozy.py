#!/usr/bin/env python3
""" concatenates two matrices """
matCon = []


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices """
    if axis == 0:
        matCon.clear()
        for i in range(len(mat1)):
            matCon.append(mat1[i])
        for j in range(len(mat2)):
            matCon.append(mat2[j])
        return matCon
    if axis == 1:
        matCon.clear()
        for i in range(len(mat1)):
            matCon.append(mat1[i])
        for j in range(len(mat2)):
            for k in range(len(mat2[j])):
                matCon[j].append(mat2[j][k])
        return matCon
