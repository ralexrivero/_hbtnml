#!/usr/bin/env python3
""" add matrices """


def matrix_shape(matrix):
    """ Shape size of a matrix """
    shape = []
    if matrix != []:
        while isinstance(matrix, list):
            shape.append(len(matrix))
            matrix = matrix[0]
    return shape


def add_matrices(mat1, mat2):
    """ add two matrices """
    # shape control
    s1 = matrix_shape(mat1)
    s2 = matrix_shape(mat2)

    if s1 != s2:
        return None

    res = []
    ndim = len(s1)

    if ndim == 1:
        for i in range(s1[0]):
            res.append(mat1[i] + mat2[i])
    elif ndim == 2:
        for i in range(s1[0]):
            res.append([])
            for j in range(s1[1]):
                res[i].append(mat1[i][j] + mat2[i][j])
    elif ndim == 3:
        for i in range(s1[0]):
            res.append([])
            for j in range(s1[1]):
                res[i].append([])
                for k in range(s1[2]):
                    res[i][j].append(mat1[i][j][k] + mat2[i][j][k])
    elif ndim == 4:
        for i in range(s1[0]):
            res.append([])
            for j in range(s1[1]):
                res[i].append([])
                for k in range(s1[2]):
                    res[i][j].append([])
                    for m in range(s1[3]):
                        res[i][j][k].append(
                            mat1[i][j][k][m] + mat2[i][j][k][m])
    else:
        return

    return res
