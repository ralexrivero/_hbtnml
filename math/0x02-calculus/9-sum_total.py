#!/usr/bin/env python3
""" calculates summation of squared """


def summation_i_squared(n):
    """ calculates summation of squared """
    if not isinstance(n, (int, float)) or n < 1:
        return None  # check the valid number

    if n == 1:
        return 1
    else:
        return summation_i_squared(n - 1) + (n * n)
