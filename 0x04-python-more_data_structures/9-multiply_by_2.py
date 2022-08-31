#!/usr/bin/python3
# 9-multiple_by_2.py


def multiply_by_2(dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: dictionary[k] * 2 for k in dictionary})
