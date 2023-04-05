#!/usr/bin/python3
'''
A module that contains a function that multiplies 2 matrices
'''
import numpy as just


def lazy_matrix_mul(m_a, m_b):
    ''' The function that multiplies 2 matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    '''

    return (just.matmul(m_a, m_b))
