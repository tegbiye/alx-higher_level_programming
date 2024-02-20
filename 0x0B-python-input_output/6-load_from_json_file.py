#!/usr/bin/python3
'''
Import module json
'''


import json
'''
load from json
'''


def load_from_json_file(filename):
    '''
    load from json
    '''
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
