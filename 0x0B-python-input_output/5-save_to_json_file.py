#!/usr/bin/python3
'''
Import module json
'''


import json
'''
save to json
'''


def save_to_json_file(my_obj, filename):
    '''
    save to json
    '''
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
