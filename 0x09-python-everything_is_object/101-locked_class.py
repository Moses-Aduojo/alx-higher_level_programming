#!/usr/bin/python3
"""
contain a class LockedClass with no class or object attribute, that\
prevents the user from dynamically creating new instance attributes,\
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """A class with restricted attribute creation.

    Attributes:
        first_name (str): The first name attribute allowed to be set.
    """

    __slots__ = ['first_name']

    def __init__(self):
        pass
