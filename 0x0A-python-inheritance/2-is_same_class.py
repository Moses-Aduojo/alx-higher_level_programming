#!/usr/bin/python3
"""
determine if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    is_same_class - determine object instance of a class
    args:
        obj - object whose class is to be confirmed
        a_class - a class of which obj is probably an instance or not
    Return - True if obj is an instance of a_class; False otherwise
    """
    return(isinstance(obj, a_class))
