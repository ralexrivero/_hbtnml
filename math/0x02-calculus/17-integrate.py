#!/usr/bin/env python3
""" calculates the integral of a polynomial"""


def poly_integral(poly, C=0):
    """ return of a polynomial """
    if not isinstance(poly, list) or poly is None:
        return None
    if C is None or not isinstance(C, int):
        return None
    polyInt = []
    polyInt.append(C)
    for i, coef in enumerate(poly):
        integral = (coef / (i + 1))
        if float(integral).is_integer():
            integral = int(integral)
        polyInt.append(integral)
    return polyInt
