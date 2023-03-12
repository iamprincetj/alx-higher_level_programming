#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = ()
    tuplea1 = tuple_a + (0, 0)
    tupleb1 = tuple_b + (0, 0)
    tuple_sum = tuplea1[0] + tupleb1[0], tuplea1[1] + tupleb1[1]
    return tuple_sum
