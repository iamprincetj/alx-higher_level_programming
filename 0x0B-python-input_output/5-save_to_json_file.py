#!/usr/bin/python3
'''A module that contains a function that does another json stuff'''
import json


def save_to_json_file(my_obj, filename):
    '''The function that writes an Object to a text file,
        using a JSON representation
    Arguments:
        my_obj: the object
        filename: the file
    '''

    with open(filename, 'w') as fil:
        json.dump(my_obj, fil)
