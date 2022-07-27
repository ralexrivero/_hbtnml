#!/usr/bin/env python3
""" transpose matrix """


def matrix_transpose(matrix):
    """ transpose matrix """
    transposed = []
    for x in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[x])
        transposed.append(transposed_row)
    return transposed
