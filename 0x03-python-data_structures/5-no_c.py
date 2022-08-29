#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    cpy = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(cpy))
