"""
This module define base class for rectangle class
"""


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
