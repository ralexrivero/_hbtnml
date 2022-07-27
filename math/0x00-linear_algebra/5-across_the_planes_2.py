#!/usr/bin/env python3
""" add two matrices """
sum = []
sumSub = []


def add_matrices2D(mat1, mat2):
    """ add two matrices """
    if len(mat1[0]) != len(mat2[0]):
        return None
    for i in range(len(mat1)):
        for j in range(len(mat1[i])):
            sumSub.append(mat1[i][j] + mat2[i][j])
        sum.append(sumSub[:])
        sumSub.clear()
    return sum
