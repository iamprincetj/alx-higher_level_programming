#!/usr/bin/python3
'''A module that contains a function that append'''


def append_after(filename="", search_string="", new_string=""):
    '''The function that inserts a line of text to a file
    Arguments:
        filename: the file to append to
        search_string: the specific string
        new_strings: the new string to append in
    '''

    new_line = ""
    with open(filename, 'r') as fil:
        for line in fil:
            new_line += line
            if search_string in line:
                new_line += new_string

    with open(filename, 'w') as fil:
        fil.write(new_line)
