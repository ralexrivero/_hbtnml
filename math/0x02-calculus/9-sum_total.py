#!/usr/bin/env python3
""" calculates summation of squared """
sum = 0


def summation_i_squared(n):
    """ calculates summation of squared """
    if not isinstance(n, (int, float)):
        return None  # check the valid number

    sum = n * (n + 1) * (2 * n + 1) / 6

    return int(sum)
