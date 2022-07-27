#!/usr/bin/env python3
""" transpose matrix using list comprehension """


def matrix_transpose(matrix):
    """ transpose matrix """
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed
