#!/usr/bin/python3
"""
This module define base class for rectangle class
"""


import json


class Base:
    """
    this is the Base class provide attrinute and methods for a
    rectangle
    """
    __nb_objects = 0

    """
    intitializes public instance attribute
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json list representaion of list_dictionary
        parameter: list_dictionaries - a list of dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
