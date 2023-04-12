#!/usr/bin/python3
'''A module that contains a Pascal's Triangle function'''


def pascal_triangle(n):
    '''The pascal triangle function
    Argument: n: the size of the triangle
    Return: multi-demensional list of integers
    '''
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(my_list[i-1][j-1] + my_list[i-1][j])
        row.append(1)
        my_list.append(row)
    return my_list
