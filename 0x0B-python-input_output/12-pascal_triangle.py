#!/usr/bin/python3
'''
Pasical Triangle
'''


def pascal_triangle(n):
    '''
     Pasical Triangle
    '''
    lst = []
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        lst.append(trow)
        trow = [ls + r for ls, r in zip(trow + y, y + trow)]
    return lst
