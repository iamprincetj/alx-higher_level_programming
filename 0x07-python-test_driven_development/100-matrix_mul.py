#!/usr/bin/python3
'''A module that contains a funtion that multiplies two matrices '''


def matrix_mul(m_a, m_b):
    '''The function that multiplies the two matices
    Arguments:
        m_a: first matrice
        m_b: second matice

    Returns:
        the result of the two matrices in a new list

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    
    '''

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if not isinstance(elements, list):
            raise TypeError("m_a must be a list of lists")

    for elements in m_b:
        if not isinstance(elements, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elements in lists:
            if not type(elements) in (float, int):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elements in lists:
            if not type(elements) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    len_list = 0

    for elements in m_a:
        if len_list != 0 and len_list != len(elements):
            raise TypeError("each row of m_a must be of the same size")
        len_list = len(elements)

    len_list = 0

    for elements in m_b:
        if len_list != 0 and len_list != len(elements):
            raise TypeError("each row of m_b must be of the same size")
        len_list = len(elements)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    list_r1 = []
    list_i1 = 0

    for a in m_a:
        list_r2 = []
        list_i2 = 0
        num = 0
        while (list_i2 < len(m_b[0])):
            num += a[list_i1] * m_b[list_i1][list_i2]
            if list_i1 == len(m_b) - 1:
                list_i1 = 0
                list_i2 += 1
                list_r2.append(num)
                num = 0
            else:
                list_i1 += 1
        list_r1.append(list_r2)

    return list_r1
