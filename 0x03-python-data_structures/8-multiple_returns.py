#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sent):
    """Returns the length of a string and its first character."""
    if sent == "":
        return (0, None)
    return (len(sent), sent[0])
