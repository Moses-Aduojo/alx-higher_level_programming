#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence or sentence is None: # if len(str_) == 0:
        a = None
    else:
        a = sentence[0]
    str_len = len(sentence)
    return (str_len, a)
