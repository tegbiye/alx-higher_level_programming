#!/usr/bin/python3
# 100-weighte_average.py

def weight_average(my_list=[]):
    sum = 0
    weightsum = 0
    if len(my_list) == 0:
        return (0)
    for tp in my_list:
        prod = 1
        weightsum += tp[1]
        for i in tp:
            prod *= i
        sum += prod
        prod = 1

    aver = sum / weightsum
    return aver
