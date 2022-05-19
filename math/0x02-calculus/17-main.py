#!/usr/bin/env python3

poly_integral = __import__('17-integrate').poly_integral

poly = [5, 3, 0, 1]
print(poly_integral(poly))

# main_0 normal
print(poly_integral([7, 4, 6, 1, 5]))
print(poly_integral([4, 8, 2, 4, 7, 1, 9], C=5))

# main_1 skipped powers
print(poly_integral([6, 5, 0, 0, -3]))
print(poly_integral([0, 0, 3, -1, 0, 6, 2], C=6))

# main_4 only a constant
print(poly_integral([5]))
print(poly_integral([5], C=7))

# main_2 poly is [0]
print(poly_integral([0]))
print(poly_integral([0], C=7))

# main_3 invalid poly
print(poly_integral(5))
print(poly_integral([]))
print(poly_integral([5], C=None))
