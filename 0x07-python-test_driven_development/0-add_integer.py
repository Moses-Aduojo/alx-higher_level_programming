#!/usr/bin/python3


"""
this modules perform basic binary arithmetic operation
"""


def add_integer(a, b=98):
    """
    add_integer: compute sum of any two given integer

    args:
        a: an integer or float
        b: an integer or float with default value of 98

    Return: the  sum of a and b in integer
    """
    if a == 'NaN':
        a = float(a)
    if b == 'NaN':
        b == float(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or b != b:
        raise ValueError('cannot convert float NaN to integer')

    a = int(a)
    b = int(b)

    return a + b
