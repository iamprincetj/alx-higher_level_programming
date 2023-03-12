#!/usr/bin/python3

def multiple_returns(sentence):
    word_len = len(sentence)
    tuple_word = ()
    if word_len == 0:
        tuple_word = 0, None
    else:
        tuple_word = word_len, sentence[0]
    return tuple_word
