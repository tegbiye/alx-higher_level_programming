#!/usr/bin/python3
'''
Append and write
'''


def append_write(filename="", text=""):
    '''
    Append and write
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
