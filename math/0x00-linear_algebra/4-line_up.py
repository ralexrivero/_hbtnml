#!/usr/bin/env python3
""" adds two arrays """
res = []


def add_arrays(arr1, arr2):
    """ add two arrays element-wise """
    if len(arr1) != len(arr2):
        return None
    for i in range(len(arr1)):
        res.append(arr1[i] + arr2[i])
    return res
