#!/usr/bin/env python3
""" calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ calculates the derivative of a polynomial """
    if not isinstance(poly, list) or poly is None:
        return None
    if len(poly) == 1:
        return [0]
    if len(poly) == 0:
        return None

    deri = []
    for i, coef in enumerate(poly):
        if i > 0:
            deri.append(coef * i)
    return deri
