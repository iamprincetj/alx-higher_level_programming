#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict_key = a_dictionary.keys()
    new_dict = {}
    for i in dict_key:
        new_dict.append(a_dictionary.get(i) * 2)
    return new_dict
