#!/usr/bin/env python3
""" concatenate two matrices along a specific axis """


def matrix_shape(matrix):
    """ Shape size of a matrix """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def cat_matrices(mat1, mat2, axis=0):
    """ concatenate two matrices along a specific axis """
    # size control
    cated = []
    s1 = matrix_shape(mat1)
    s2 = matrix_shape(mat2)

    ndim = len(s1)

    if s1 != s2:  # control shape
        return None
    elif ndim <= axis:  # control axis on dimension
        return None
    elif ndim == 1:  # 1D Array
        if axis == 0:
            cated = mat1 + mat2
        else:
            return None
    elif ndim == 2:  # 2D Array
        if axis == 0:
            for row1 in mat1:
                cated.append(row1)
            for row2 in mat2:
                cated.append(row2)
        elif axis == 1:
            for i in range(s1[0]):
                cated.append(mat1[i] + mat2[i])
        else:
            return None
    elif ndim == 3:  # 3D Array
        if axis == 0:
            for row1 in mat1:
                cated.append(row1)
            for row2 in mat2:
                cated.append(row2)
        elif axis == 1:
            for i in range(s1[0]):
                cated[i].append(mat1[i] + mat2[i])
        elif axis == 2:
            for i in range(s1[0]):
                for j in range(s1[1]):
                    cated.append([mat1[i][j] + mat2[i][j]])
        else:
            return
    elif ndim == 4:  # 4D Array
        if axis == 0:
            for row1 in mat1:
                cated.append(row1)
            for row2 in mat2:
                cated.append(row2)
        elif axis == 1:
            for i in range(s1[0]):
                cated.append([])
                cated[i].append(mat1[i] + mat2[i])
        elif axis == 2:
            for i in range(s1[0]):
                cated.append([])
                for j in range(s1[1]):
                    cated[i].append([])
                    cated.append(mat1[i][j] + mat2[i][j])
        elif axis == 3:
            for i in range(s1[0]):
                cated.append([])
                for j in range(s1[1]):
                    cated[i].append([])
                    for k in range(s1[2]):
                        cated[i][j].append(mat1[i][j][k] + mat2[i][j][k])
        else:
            return
    else:
        return cated  # Not handled more than 4 dimensional arrays

    return cated
