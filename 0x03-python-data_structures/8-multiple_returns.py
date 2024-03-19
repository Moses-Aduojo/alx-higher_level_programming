#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        a = None
        str_len = 0
    else:
        a = sentence[0]
        str_len = len(sentence)
    return (str_len, a)
